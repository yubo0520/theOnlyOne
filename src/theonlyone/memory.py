from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class MemoryCard:
    title: str
    body: str
    source: str
    path: Path


def load_cards(directory: Path) -> list[MemoryCard]:
    if not directory.is_dir():
        return []
    cards = []
    for path in sorted(directory.glob("*.md")):
        body = path.read_text(encoding="utf-8").strip()
        if not body:
            continue
        title_match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
        cards.append(
            MemoryCard(
                title=title_match.group(1).strip() if title_match else path.stem,
                body=body,
                source=path.name,
                path=path,
            )
        )
    return cards


def _terms(text: str) -> set[str]:
    clean = re.sub(r"\s+", "", text.lower())
    terms = set(re.findall(r"[a-z0-9_]{2,}", clean))
    terms.update(clean[index : index + 2] for index in range(max(0, len(clean) - 1)))
    return {term for term in terms if term.strip()}


def retrieve(cards: list[MemoryCard], query: str, limit: int = 5) -> list[MemoryCard]:
    query_terms = _terms(query)
    if not query_terms:
        return cards[:limit]
    ranked = []
    for card in cards:
        title_terms = _terms(card.title)
        body_terms = _terms(card.body)
        score = len(query_terms & body_terms) + 3 * len(query_terms & title_terms)
        ranked.append((score, card.title, card))
    ranked.sort(key=lambda item: (-item[0], item[1]))
    return [card for score, _, card in ranked if score > 0][:limit]


def format_cards(cards: list[MemoryCard]) -> str:
    if not cards:
        return ""
    blocks = ["# Relevant character memories\nUse only when relevant. Do not invent missing canon facts."]
    for card in cards:
        blocks.append(f'<memory title="{card.title}" source="{card.source}">\n{card.body}\n</memory>')
    return "\n\n".join(blocks)

