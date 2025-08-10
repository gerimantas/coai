import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_orchestrator_status_endpoint(client):
    response = client.get('/api/orchestrator/status')
    assert response.status_code == 200
    data = response.get_json()
    assert 'orchestrator_status' in data
    assert 'components' in data
    assert 'version' in data
    assert 'capabilities' in data
    assert isinstance(data['components'], dict)
    assert isinstance(data['capabilities'], list)
