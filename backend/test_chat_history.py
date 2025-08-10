import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_chat_history_endpoint(client):
    response = client.get('/api/chat/history')
    assert response.status_code == 200
    data = response.get_json()
    assert 'history' in data
    assert 'count' in data
    assert isinstance(data['history'], list)
    assert isinstance(data['count'], int)

def test_chat_history_endpoint_error(client, monkeypatch):
    # Simulate error in logger
    import sys
    import types
    from app import routes
    def error_logger(limit):
        raise Exception('Logger error')
    monkeypatch.setattr(routes.coai_logger, 'get_chat_history', error_logger)
    response = client.get('/api/chat/history')
    assert response.status_code == 500
    data = response.get_json()
    assert 'error' in data
