#!/usr/bin/env python3
"""Windows regression tests for local-coder server identity checks."""

from __future__ import annotations

import os
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
from urllib.request import urlopen

LAUNCHER = Path(__file__).resolve().parents[1] / "launch.ps1"

FAKE_SERVER_SOURCE = r"""
import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True)
parser.add_argument("--model-id", required=True)
parser.add_argument("-m", "--model", required=True)
args = parser.parse_args()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = b'{"status":"ok"}'
        elif self.path == "/v1/models":
            body = json.dumps({"data": [{"id": args.model_id}]}).encode()
        else:
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *values):
        return

ThreadingHTTPServer(("127.0.0.1", args.port), Handler).serve_forever()
"""


@unittest.skipUnless(os.name == "nt", "launcher is Windows-only")
class LaunchIdentityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.fake_server = self.root / "fake_server.py"
        self.fake_server.write_text(FAKE_SERVER_SOURCE, encoding="utf-8")
        self.server_process: subprocess.Popen[str] | None = None
        self.port: int | None = None

    def tearDown(self) -> None:
        if self.server_process is not None and self.server_process.poll() is None:
            self.server_process.terminate()
            try:
                self.server_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.server_process.kill()
                self.server_process.wait(timeout=5)
        self.temporary.cleanup()

    def start_fake_server(
        self, command_model: Path, model_id: str, model_flag: str = "-m"
    ) -> None:
        with socket.socket() as probe:
            probe.bind(("127.0.0.1", 0))
            self.port = probe.getsockname()[1]

        process_executable = getattr(sys, "_base_executable", sys.executable)
        self.server_process = subprocess.Popen(
            [
                process_executable,
                str(self.fake_server),
                "--port",
                str(self.port),
                "--model-id",
                model_id,
                model_flag,
                str(command_model),
            ],
            text=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            if self.server_process.poll() is not None:
                self.fail(
                    f"fake server exited early with code {self.server_process.returncode}"
                )
            try:
                with urlopen(f"http://127.0.0.1:{self.port}/health", timeout=0.5) as response:
                    if response.status == 200:
                        return
            except OSError:
                time.sleep(0.05)
        self.fail("fake server did not become ready")

    def run_launcher(self, model: Path) -> subprocess.CompletedProcess[str]:
        self.assertIsNotNone(self.port)
        process_executable = getattr(sys, "_base_executable", sys.executable)
        return subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-ExecutionPolicy",
                "Bypass",
                "-File",
                str(LAUNCHER),
                "-Port",
                str(self.port),
                "-ServerPath",
                process_executable,
                "-ModelPath",
                str(model),
                "-LlamaDir",
                str(model.parent),
                "-NoBrowser",
            ],
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            check=False,
        )

    def test_reuses_only_matching_executable_and_model(self) -> None:
        model = self.root / "expected.gguf"
        model.touch()
        self.start_fake_server(model, model.name, "--model")
        result = self.run_launcher(model)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("intended model", result.stdout)

    def test_rejects_listener_with_wrong_model(self) -> None:
        model = self.root / "expected.gguf"
        model.touch()
        self.start_fake_server(model, "different.gguf")
        result = self.run_launcher(model)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("expected model", result.stdout)

    def test_rejects_same_basename_model_from_wrong_directory(self) -> None:
        expected_model = self.root / "expected" / "same-name.gguf"
        wrong_model = self.root / "wrong" / "same-name.gguf"
        expected_model.parent.mkdir()
        wrong_model.parent.mkdir()
        expected_model.touch()
        wrong_model.touch()
        self.start_fake_server(wrong_model, expected_model.name)

        result = self.run_launcher(expected_model)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("expected exact path", result.stdout)
        self.assertIn(str(wrong_model), result.stdout)

    def test_timeout_path_stops_exact_owned_process(self) -> None:
        text = LAUNCHER.read_text(encoding="utf-8")
        self.assertIn("Stop-Process -Id $proc.Id -Force", text)
        self.assertNotIn("Stop-Process -Name", text)


if __name__ == "__main__":
    unittest.main()
