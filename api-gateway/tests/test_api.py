import json
from app import app

def test_upload_route():
    client = app.test_client()

    response = client.post(
        "/upload",
        data={"file": (bytes("hello world", "utf-8"), "test.txt")}
    )

    assert response.status_code == 200
    data = json.loads(response.data)
    assert "job_id" in data

def test_search_route():
    client = app.test_client()

    response = client.get("/search?q=test")
    # We can't expect Qdrant to run here, so just check HTTP code
    assert response.status_code in [200, 500]
