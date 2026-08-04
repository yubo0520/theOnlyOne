# Security and privacy

Do not open public issues containing API keys, private conversations, voice samples, or copyrighted character data.

The repository ignores runtime data, character packs, audio, models, databases, logs, and environment files. Secrets must be supplied through environment variables or an untracked `.env` file.

Before publishing a commit, run `scripts/security-check.ps1` and inspect `git diff --cached` manually.

