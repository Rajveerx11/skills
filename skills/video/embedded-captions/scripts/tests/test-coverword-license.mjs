#!/usr/bin/env node

import assert from "node:assert/strict";
import { execFile } from "node:child_process";
import { mkdtemp, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { promisify } from "node:util";

const execFileAsync = promisify(execFile);
const here = dirname(fileURLToPath(import.meta.url));
const compiler = resolve(here, "..", "make-theme.cjs");
const project = await mkdtemp(join(tmpdir(), "coverword-license-test-"));

try {
  await writeFile(
    join(project, "theme.json"),
    JSON.stringify({ dna: "nightcity", lines: [], duration: 1 }),
    "utf8",
  );
  await writeFile(join(project, "transcript.json"), '{"words":[]}', "utf8");
  let error;
  try {
    await execFileAsync(process.execPath, [compiler, project]);
  } catch (caught) {
    error = caught;
  }
  assert(error, "nightcity must fail closed without its licensed font");
  const output = `${error.stdout || ""}\n${error.stderr || ""}`;
  assert.match(output, /requires a user-supplied, appropriately licensed/);
  assert.doesNotMatch(output, /ENOENT/);
  console.log("coverword license preflight test passed");
} finally {
  await rm(project, { recursive: true, force: true });
}
