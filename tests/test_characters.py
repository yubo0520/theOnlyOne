from pathlib import Path

from ohmylover.characters import CharacterStore


def test_demo_character_loads():
    root = Path(__file__).resolve().parents[1] / "examples"
    pack = CharacterStore(root).get("demo-character")
    assert pack.name == "林川"
    assert "虚构" in pack.persona


def test_path_traversal_is_rejected():
    root = Path(__file__).resolve().parents[1] / "examples"
    store = CharacterStore(root)
    for invalid in ("../private", "a/b", "a\\b"):
        try:
            store.get(invalid)
        except KeyError:
            pass
        else:
            raise AssertionError(f"accepted invalid character id: {invalid}")

