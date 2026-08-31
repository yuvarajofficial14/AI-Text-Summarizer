def test_create_summary(client, monkeypatch):
    async def mock_generate(text):
        return "Mocked summary"

    monkeypatch.setattr(
        "app.routers.summary.generate_summary",
        mock_generate
    )

    response = client.post(
        "/summaries",
        json={
            "text": "This is a long input text used for testing. " * 5
        }
    )

    assert response.status_code == 201
    assert response.json()["summary_text"] == "Mocked summary"


def test_update_summary(client, monkeypatch):
    async def mock_generate(text):
        return "Mocked summary"

    monkeypatch.setattr(
        "app.routers.summary.generate_summary",
        mock_generate
    )

    create_response = client.post(
        "/summaries",
        json={
            "text": "Testing update functionality. " * 5
        }
    )

    assert create_response.status_code == 201

    summary_id = create_response.json()["id"]

    update_response = client.put(
        f"/summaries/{summary_id}",
        json={
            "summary_text": "Updated summary"
        }
    )

    assert update_response.status_code == 200
    assert update_response.json()["summary_text"] == "Updated summary"


def test_get_summary(client, monkeypatch):
    async def mock_generate(text):
        return "Mocked summary"

    monkeypatch.setattr(
        "app.routers.summary.generate_summary",
        mock_generate
    )

    create_response = client.post(
        "/summaries",
        json={
            "text": "Testing GET functionality. " * 5
        }
    )

    summary_id = create_response.json()["id"]

    get_response = client.get(
        f"/summaries/{summary_id}"
    )

    assert get_response.status_code == 200
    assert get_response.json()["summary_text"] == "Mocked summary"


def test_delete_summary(client, monkeypatch):
    async def mock_generate(text):
        return "Mocked summary"

    monkeypatch.setattr(
        "app.routers.summary.generate_summary",
        mock_generate
    )

    create_response = client.post(
        "/summaries",
        json={
            "text": "Testing DELETE functionality. " * 5
        }
    )

    summary_id = create_response.json()["id"]

    delete_response = client.delete(
        f"/summaries/{summary_id}"
    )

    assert delete_response.status_code == 204


def test_get_deleted_summary_returns_404(client):
    response = client.get("/summaries/999999")

    assert response.status_code == 404
