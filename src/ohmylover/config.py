from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    root: Path
    character_dir: Path
    llm_base_url: str
    llm_api_key: str
    llm_model: str
    voice_service_url: str
    memory_top_k: int
    host: str
    port: int

    @classmethod
    def load(cls) -> Settings:
        load_dotenv()
        root = Path(__file__).resolve().parents[2]
        character_dir = Path(os.getenv("OML_CHARACTER_DIR", "examples"))
        if not character_dir.is_absolute():
            character_dir = root / character_dir
        return cls(
            root=root,
            character_dir=character_dir.resolve(),
            llm_base_url=os.getenv("OML_LLM_BASE_URL", "https://api.openai.com/v1").rstrip("/"),
            llm_api_key=os.getenv("OML_LLM_API_KEY", "").strip(),
            llm_model=os.getenv("OML_LLM_MODEL", "gpt-4.1-mini").strip(),
            voice_service_url=os.getenv("OML_VOICE_SERVICE_URL", "").strip().rstrip("/"),
            memory_top_k=max(1, int(os.getenv("OML_MEMORY_TOP_K", "5"))),
            host=os.getenv("OML_HOST", "127.0.0.1"),
            port=int(os.getenv("OML_PORT", "8000")),
        )

