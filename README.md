# ohMyLover

> [!IMPORTANT]
> **Demo / Work in Progress** — ohMyLover is an early technical prototype under active construction. It is not a finished application, hosted service, or production-ready AI companion. APIs, data formats, and architecture may change.

**ohMyLover** is a local-first character-agent engine for experimenting with grounded personas, retrievable character memories, streaming conversation, and optional voice services.

This is the sanitized, character-agnostic engine. It intentionally contains no private conversations, cloned voices, model weights, scraped scripts, or copyrighted character packs.

This public repository is a clean-room demo of the reusable engine architecture. It is not a public copy of the author's private character project. The included character is fictional and exists only to demonstrate the pack format.

## Included

- Character packs kept separate from engine code
- Persona and memory-card loading
- Lightweight local memory retrieval
- OpenAI-compatible streaming chat
- Optional proxy to an external ASR/TTS service
- A fictional demo character, tests, CI, and privacy checks

## Not included

- Model weights, inference binaries, cloned voices, private history, or third-party character assets
- A production frontend

## Quick start

Requires Python 3.10+.

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
Copy-Item .env.example .env
```

Set the provider values in `.env`, then run:

```powershell
ohmylover
```

Open `http://127.0.0.1:8000/api/status`.

## API

- `GET /api/status`
- `GET /api/characters`
- `POST /api/chat` (Server-Sent Events)
- `/api/voice/*` (optional external voice-service proxy)

```json
{
  "character_id": "demo-character",
  "messages": [{"role": "user", "content": "今天过得怎么样？"}]
}
```

Character data can stay in a private directory selected by `OML_CHARACTER_DIR`. See [Character packs](docs/CHARACTER_PACKS.md).

Before publishing changes, run:

```powershell
.\scripts\security-check.ps1
```

## Status

🚧 **Under construction.** The current repository demonstrates only the basic engine boundary: character-pack loading, lightweight memory retrieval, provider-compatible streaming chat, and an optional voice-service proxy.

Not yet included: a production frontend, persistent user memory, advanced RAG, a character decision layer, desktop-pet UI, voice inference implementation, deployment hardening, or multi-user accounts.

## License

MIT. The license covers only repository code, not external packs, media, voices, model weights, or services.
