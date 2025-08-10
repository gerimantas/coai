import pytest
from backend.app import routes
from backend.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_chat_endpoint(client):
    response = client.post('/api/chat', json={"message": "Hello"})
    assert response.status_code == 200
    data = response.get_json()
    assert "reply" in data

def test_file_read_endpoint(client):
    # Test with a known file (README.md)
    response = client.get('/api/files/README.md')
    assert response.status_code in (200, 404)  # 404 if file not found
    # If found, check content
    if response.status_code == 200:
        assert "COAI" in response.get_data(as_text=True)
