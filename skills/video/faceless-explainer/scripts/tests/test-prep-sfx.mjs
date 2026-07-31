import assert from "node:assert/strict";
import {
  existsSync,
  mkdirSync,
  mkdtempSync,
  readFileSync,
  rmSync,
  writeFileSync,
} from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { spawnSync } from "node:child_process";
import test from "node:test";

const implementations = [
  {
    name: "faceless-explainer",
    url: new URL("../lib/prep-sfx.mjs", import.meta.url),
  },
  {
    name: "pr-to-video",
    url: new URL("../../../pr-to-video/scripts/lib/prep-sfx.mjs", import.meta.url),
  },
];

function fixture() {
  const root = mkdtempSync(join(tmpdir(), "prep-sfx-"));
  const library = join(root, "library");
  const project = join(root, "project");
  return { root, library, project };
}

for (const implementation of implementations) {
  test(`${implementation.name}: empty manifest is a clean no-op`, async () => {
    const { root, library, project } = fixture();
    try {
      mkdirSync(library, { recursive: true });
      writeFileSync(join(library, "manifest.json"), "{}\n");
      const { resolveSfx } = await import(implementation.url);
      const anomalies = [];
      const sfx = resolveSfx({
        sfxLibDir: library,
        hyperframesDir: project,
        scenes: [{ sceneId: "scene-1", sfxCues: [{ file: "missing.mp3", t_local: 0 }] }],
        groups: [],
        anomalies,
      });
      assert.deepEqual(sfx, []);
      assert.equal(existsSync(join(project, "assets", "sfx")), false);
      assert.match(anomalies.join("\n"), /manifest is empty/);
    } finally {
      rmSync(root, { recursive: true, force: true });
    }
  });

  test(`${implementation.name}: missing declared source fails before copy`, () => {
    const { root, library, project } = fixture();
    try {
      mkdirSync(library, { recursive: true });
      writeFileSync(
        join(library, "manifest.json"),
        JSON.stringify({ missing: { file: "missing.mp3", duration: 1 } }),
      );
      const source = `
        import { resolveSfx } from ${JSON.stringify(implementation.url.href)};
        resolveSfx({
          sfxLibDir: process.argv[1],
          hyperframesDir: process.argv[2],
          scenes: [],
          groups: [],
          anomalies: [],
        });
      `;
      const result = spawnSync(
        process.execPath,
        ["--input-type=module", "--eval", source, library, project],
        { encoding: "utf8" },
      );
      assert.equal(result.status, 1);
      assert.match(result.stderr, /source file missing/);
      assert.equal(existsSync(join(project, "assets", "sfx")), false);
    } finally {
      rmSync(root, { recursive: true, force: true });
    }
  });

  test(`${implementation.name}: valid external library copies declared files`, async () => {
    const { root, library, project } = fixture();
    try {
      mkdirSync(library, { recursive: true });
      writeFileSync(
        join(library, "manifest.json"),
        JSON.stringify({ hit: { file: "hit.mp3", duration: 1.5 } }),
      );
      writeFileSync(join(library, "hit.mp3"), "test-audio");
      writeFileSync(join(library, "CREDITS.md"), "licensed test fixture\n");

      const { resolveSfx } = await import(implementation.url);
      const sfx = resolveSfx({
        sfxLibDir: library,
        hyperframesDir: project,
        scenes: [
          {
            sceneId: "scene-1",
            sfxCues: [{ file: "hit.mp3", t_local: 0.25, volume: 0.4, note: "hit" }],
          },
        ],
        groups: [
          {
            scene_ids: ["scene-1"],
            scenes: { "scene-1": { start_s: 2 } },
          },
        ],
        anomalies: [],
      });

      assert.equal(sfx.length, 1);
      assert.equal(sfx[0].t, 2.25);
      assert.equal(sfx[0].duration, 1.5);
      assert.equal(readFileSync(join(project, "assets", "sfx", "hit.mp3"), "utf8"), "test-audio");
      assert.equal(existsSync(join(project, "assets", "sfx", "manifest.json")), true);
      assert.equal(existsSync(join(project, "assets", "sfx", "CREDITS.md")), true);
    } finally {
      rmSync(root, { recursive: true, force: true });
    }
  });
}
