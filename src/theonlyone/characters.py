from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CharacterPack:
    id: str
    name: str
    description: str
    default_voice: str
    directory: Path
    persona: str

    @property
    def memory_dir(self) -> Path:
        return self.directory / "memory_cards"


class CharacterStore:
    def __init__(self, root: Path):
        self.root = root

    def list(self) -> list[CharacterPack]:
        if not self.root.is_dir():
            return []
        packs = []
        for manifest in sorted(self.root.glob("*/character.json")):
            try:
                packs.append(self._load(manifest))
            except (OSError, ValueError, json.JSONDecodeError):
                continue
        return packs

    def get(self, character_id: str) -> CharacterPack:
        safe_id = character_id.strip()
        if not safe_id or any(value in safe_id for value in ("/", "\\", "..")):
            raise KeyError(character_id)
        manifest = self.root / safe_id / "character.json"
        if not manifest.is_file():
            raise KeyError(character_id)
        pack = self._load(manifest)
        if pack.id != safe_id:
            raise ValueError("character.json id must match its directory name")
        return pack

    @staticmethod
    def _load(manifest: Path) -> CharacterPack:
        data = json.loads(manifest.read_text(encoding="utf-8"))
        directory = manifest.parent.resolve()
        persona_path = directory / str(data.get("persona", "persona.md"))
        return CharacterPack(
            id=str(data["id"]),
            name=str(data["name"]),
            description=str(data.get("description", "")),
            default_voice=str(data.get("default_voice", "")),
            directory=directory,
            persona=persona_path.read_text(encoding="utf-8").strip(),
        )

