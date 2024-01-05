import json

    
# GET /books
def test_authors_page(client):
    response = client.get("/authors")
    assert response.status_code == 200

    
# GET/:id authors
def test_author_page(client):
    response = client.get('/authors/1')
    err_response = client.get('/authors/68')
    assert err_response.status_code == 404
    assert response.status_code == 200
    
    data = json.loads(response.data)["data"]
    assert data['id'] == 1


def test_create_author(client):
    data = {
        "name": "New Author"
    }
    response = client.post('/authors', json=data)
    assert response.status_code == 201
    created_data = json.loads(response.data)
    assert "data" in created_data



def test_create_author_error(client):
    data = {
        "title": "New author"
    }
    response = client.post('/authors', json=data)
    assert response.status_code == 400

def test_update_author(client):
    data = {
        "name": "Updated Author"
    }
    response = client.patch('/authors/1', json=data)
    assert response.status_code == 200
    updated_data = json.loads(response.data)
    assert "data" in updated_data
