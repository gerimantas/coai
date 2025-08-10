import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_file_read_endpoint_invalid_path(client):
    response = client.get('/api/files/../../secret.txt')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Neleistinas kelias'

def test_file_read_endpoint_not_found(client):
    response = client.get('/api/files/this_file_does_not_exist.txt')
    assert response.status_code == 404
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Failas nerastas'
