import json

from fastapi.testclient import TestClient

from ohmylover.main import app

client = TestClient(app)


def test_status_and_demo_character_are_available():
    status = client.get("/api/status")
    assert status.status_code == 200
    assert status.json()["ok"] is True
    assert status.json()["demo_mode"] is True

    characters = client.get("/api/characters")
    assert characters.status_code == 200
    assert [item["id"] for item in characters.json()] == ["demo-character"]


def test_demo_ui_is_served_without_private_assets():
    response = client.get("/app/")
    assert response.status_code == 200
    assert "ohMyLover Demo" in response.text
    assert "Ezreal" in response.text

    support = client.get("/app/support.js")
    assert support.status_code == 200

    assert client.get("/api/questions").json() == {"groups": []}
    assert client.get("/api/materials").json() == {"files": []}
    assert client.get("/api/favorites").json() == {"items": []}


def test_chat_stream_works_without_an_api_key_in_demo_mode():
    response = client.post(
        "/api/chat",
        json={
            "character_id": "demo-character",
            "messages": [{"role": "user", "content": "你好"}],
        },
    )
    assert response.status_code == 200
    assert 'data: {"delta":' in response.text
    chunks = []
    for line in response.text.splitlines():
        if line.startswith("data: {"):
            chunks.append(json.loads(line[6:])["delta"])
    assert "ohMyLover" in "".join(chunks)
    assert "data: [DONE]" in response.text
