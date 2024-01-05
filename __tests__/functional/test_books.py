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
    assert response.status_code == 200
    data = json.loads(response.data)["data"]
    assert data['id'] == 1

def test_book_page_not_found(client):
    err_response = client.get('/books/68')
    assert err_response.status_code == 404


# POST books
def test_create_book(client):
    data = {
        "title": "New Book",
        "author_id": 1,
        "genre": "Fiction"
    }
    response = client.post('/books', json=data)
    assert response.status_code == 201
    created_data = json.loads(response.data)
    assert "data" in created_data


def test_create_book_error(client):
    data = {
        "title": "New Book",
        "author_id": 1
    }
    response = client.post('/books', json=data)
    assert response.status_code == 400

#PATCH /books/:id
def test_update_book(client):
    data = {
        "title": "Updated Book"
    }
    response = client.patch('/books/1', json=data)
    assert response.status_code == 200
    updated_data = json.loads(response.data)
    assert "data" in updated_data

# DELETE /books/:id
def test_delete_book(client):
    response = client.delete('/books/1')
    assert response.status_code == 204  
    assert response.data == b''  

