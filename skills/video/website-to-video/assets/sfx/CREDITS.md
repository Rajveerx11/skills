# Optional SFX library

No sound-effect audio is bundled with this skill. `manifest.json` is intentionally empty.

To use SFX, set `SFX_LIB_DIR` to a separate licensed library directory. It must contain:

- `manifest.json` with one object entry per `.mp3`, including `file` and a positive `duration`;
- every audio file declared by the manifest;
- optional `CREDITS.md` or other license records.

Use only audio you created, commissioned, or are licensed to use in the intended output. Keep license evidence with the external library. If no external library is configured, omit SFX from the storyboard and build.
