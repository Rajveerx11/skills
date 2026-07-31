// prep.mjs concern module — resolve the SFX library and scene cues into globally
// timed sfx records. Split out of prep.mjs (Step 6.5). Copies the opt-in library
// into the project, validates each cue against manifest.json, and offsets each
// cue's scene-local t by its scene start_s. Appends to the shared anomalies array
// and returns the sorted sfx[] for group_spec.
import { copyFileSync, existsSync, mkdirSync, readFileSync, statSync } from "node:fs";
import { basename, join } from "node:path";
import { die } from "./prep-log.mjs";

export function loadSfxLibrary(sfxLibDir) {
  const manifestPath = join(sfxLibDir, "manifest.json");
  if (!existsSync(manifestPath)) {
    throw new Error(`--sfx-lib points to ${sfxLibDir} but manifest.json is missing`);
  }

  let manifest;
  try {
    manifest = JSON.parse(readFileSync(manifestPath, "utf8"));
  } catch (error) {
    throw new Error(`sfx manifest.json parse: ${error.message}`);
  }
  if (!manifest || Array.isArray(manifest) || typeof manifest !== "object") {
    throw new Error("sfx manifest.json must be a JSON object");
  }

  const sfxByFile = new Map();
  const sourceFiles = [];
  for (const [key, entry] of Object.entries(manifest)) {
    if (!entry || typeof entry !== "object" || Array.isArray(entry)) {
      throw new Error(`sfx manifest entry "${key}" must be an object`);
    }
    const file = entry.file;
    if (
      typeof file !== "string" ||
      !file ||
      basename(file) !== file ||
      !file.toLowerCase().endsWith(".mp3")
    ) {
      throw new Error(`sfx manifest entry "${key}" has an invalid MP3 filename`);
    }
    const duration = Number(entry.duration);
    if (!Number.isFinite(duration) || duration <= 0) {
      throw new Error(`sfx manifest entry "${key}" has an invalid duration`);
    }
    if (sfxByFile.has(file)) {
      throw new Error(`sfx manifest declares duplicate file "${file}"`);
    }
    const source = join(sfxLibDir, file);
    if (!existsSync(source) || !statSync(source).isFile()) {
      throw new Error(`sfx manifest entry "${key}" source file missing: ${source}`);
    }
    sfxByFile.set(file, { key, duration });
    sourceFiles.push(file);
  }

  return { manifestPath, sfxByFile, sourceFiles };
}

// SFX library is OPT-IN: when the orchestrator passes --sfx-lib the directory is
// copied into <PROJECT_DIR>/assets/sfx/ and section_plan **SFX:** cues are
// validated against manifest.json. Without --sfx-lib, scene cues are silently
// dropped (warning only). Voice/bgm live under assets/; SFX matches.
export function resolveSfx({ sfxLibDir, hyperframesDir, scenes, groups, anomalies }) {
  const sfx = [];
  if (sfxLibDir) {
    let library;
    try {
      library = loadSfxLibrary(sfxLibDir);
    } catch (error) {
      die(error.message);
    }

    const { sfxByFile, sourceFiles } = library;
    if (sfxByFile.size === 0) {
      const cueCount = scenes.reduce((sum, scene) => sum + (scene.sfxCues?.length || 0), 0);
      if (cueCount > 0) {
        anomalies.push(
          `section_plan declares ${cueCount} SFX cue(s) but the supplied manifest is empty — all cues dropped`,
        );
      }
      console.log("  sfx library empty: no audio copied");
      return sfx;
    }

    // Preflight above proves every declared source exists before any copy starts.
    // Copy only declared audio plus portable metadata; ignore unrelated files.
    const sfxDestDir = join(hyperframesDir, "assets", "sfx");
    mkdirSync(sfxDestDir, { recursive: true });
    let sfxCopied = 0;
    const filesToCopy = ["manifest.json", ...sourceFiles];
    if (existsSync(join(sfxLibDir, "CREDITS.md"))) filesToCopy.push("CREDITS.md");
    for (const file of filesToCopy) {
      const src = join(sfxLibDir, file);
      const dest = join(sfxDestDir, file);
      if (!existsSync(dest)) {
        copyFileSync(src, dest);
        sfxCopied++;
      }
    }

    // Resolve each scene's cues against manifest + add scene.start_s offset.
    for (const g of groups) {
      for (const sid of g.scene_ids) {
        const sceneEntry = g.scenes[sid];
        const sceneCues = scenes.find((x) => x.sceneId === sid)?.sfxCues || [];
        for (const cue of sceneCues) {
          const hit = sfxByFile.get(cue.file);
          if (!hit) {
            anomalies.push(
              `${sid}: SFX cue file "${cue.file}" not in manifest — dropping (known files: ${[...sfxByFile.keys()].slice(0, 5).join(", ")}${sfxByFile.size > 5 ? ", …" : ""})`,
            );
            continue;
          }
          const tGlobal = Number((sceneEntry.start_s + cue.t_local).toFixed(3));
          sfx.push({
            file: cue.file,
            t: tGlobal,
            duration: hit.duration,
            volume: cue.volume != null ? cue.volume : 0.35,
            scene_id: sid,
            t_local: cue.t_local,
            note: cue.note || "",
          });
        }
      }
    }
    // Sort by global t for predictable index.html emission order.
    sfx.sort((a, b) => a.t - b.t);
    console.log(`  sfx lib copied: ${sfxCopied} file(s) → assets/sfx/`);
  } else {
    // Surface plan cues that won't make it to the timeline because no lib was provided.
    let droppedCueCount = 0;
    for (const s of scenes) droppedCueCount += s.sfxCues?.length || 0;
    if (droppedCueCount > 0) {
      anomalies.push(
        `section_plan declares ${droppedCueCount} SFX cue(s) but --sfx-lib not passed — all cues dropped`,
      );
    }
  }
  return sfx;
}
