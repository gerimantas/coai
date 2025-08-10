import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_chat_endpoint_empty_message(client):
    response = client.post('/api/chat', json={"message": ""})
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "Message cannot be empty"

def test_chat_endpoint_too_long_message(client):
    long_message = "a" * 10001
    response = client.post('/api/chat', json={"message": long_message})
    assert response.status_code == 400 or response.status_code == 500
    data = response.get_json()
    assert "error" in data or "message" in data
