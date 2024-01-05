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


    
# GET/:id books
def test_book_page(client):
    response = client.get('/books/1')
    err_response = client.get('/authors/68')
    assert err_response.status_code == 404
    assert response.status_code == 200
    
    data = json.loads(response.data)["data"]
    assert data['id'] == 1


# DELETE /books/:id
def test_delete_book(client):
    response = client.delete('/books/1')
    assert response.status_code == 204  
    assert response.data == b''  

