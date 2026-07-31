# Optional SFX library

No sound-effect audio is bundled with this skill. `manifest.json` is intentionally empty.

To use SFX, provide a separate licensed library directory through `SFX_LIB_DIR`; the workflow forwards it to the shared preparation script as `--sfx-lib`. The directory must contain:

- `manifest.json` with one object entry per `.mp3`, including `file` and a positive `duration`;
- every audio file declared by the manifest;
- optional `CREDITS.md` or other license records.

Use only audio you created, commissioned, or are licensed to use in the intended output. Keep license evidence with the external library. Missing or malformed declared sources stop preparation before anything is copied.
