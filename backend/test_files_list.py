import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_files_list_endpoint_root(client):
    response = client.get('/api/files/list')
    assert response.status_code == 200
    data = response.get_json()
    assert 'tree' in data or 'children' in data
    # Check that root contains expected folders
    tree = data.get('tree') or {'children': data.get('children', [])}
    assert isinstance(tree, dict)
    assert 'children' in tree
    assert any(child['name'] == 'coai' for child in tree['children'])

def test_files_list_endpoint_forbidden(client):
    response = client.get('/api/files/list?path=../../')
    assert response.status_code == 403
    data = response.get_json()
    assert 'error' in data
