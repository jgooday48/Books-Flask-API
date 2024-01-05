import json

def test_index_page(client):
    response = client.get("/")    
    assert response.status_code == 200    

# GET /books
def test_books_page(client):
    response = client.get("/books")
    assert response.status_code == 200
    data = json.loads(response.data)["data"]
    assert type(data) == list
    assert len(data) > 1

    
# GET/:id books
def test_book_page(client):
    response = client.get('/books/2')
    assert response.status_code == 200
    
    data = json.loads(response.data)["data"]
    assert data['id'] == 2

