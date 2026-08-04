# Character packs

A character pack is a directory outside the engine:

```text
my-character/
  character.json
  persona.md
  memory_cards/
    event-001.md
```

`character.json`:

```json
{
  "id": "my-character",
  "name": "Display name",
  "description": "Short description",
  "default_voice": "optional-voice-id",
  "persona": "persona.md"
}
```

Set `THEONLYONE_CHARACTER_DIR` to the parent directory containing one or more packs.

Recommended private layers: `persona.md`, `memory_cards/`, optional source knowledge, and private voice metadata. Do not publish copyrighted scripts, media, cloned voices, or private conversations without permission.
