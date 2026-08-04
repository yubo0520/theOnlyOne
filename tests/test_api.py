from fastapi.testclient import TestClient

from ohmylover.main import app

client = TestClient(app)


def test_status_and_demo_character_are_available():
    status = client.get("/api/status")
    assert status.status_code == 200
    assert status.json()["ok"] is True

    characters = client.get("/api/characters")
    assert characters.status_code == 200
    assert [item["id"] for item in characters.json()] == ["demo-character"]

