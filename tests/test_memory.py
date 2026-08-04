from pathlib import Path

from theonlyone.memory import load_cards, retrieve


def test_retrieval_finds_relevant_card():
    root = Path(__file__).resolve().parents[1] / "examples" / "demo-character" / "memory_cards"
    cards = load_cards(root)
    result = retrieve(cards, "第一次为什么深夜还开着店", limit=1)
    assert result
    assert result[0].title == "第一次见面"
