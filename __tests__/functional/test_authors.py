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



