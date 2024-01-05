from application.books.models import Book
from application.authors.models import Author
def test_new_book():

    new_book = Book(title="Less than Zero", author_id=1)
    assert new_book.title == 'Less than Zero'


    assert new_book.json == {
        "id": new_book.id,
        "title": new_book.title,
        "author_id": new_book.author_id,
    }

def test_new_author():

    new_author = Author(name="Charles Dickens")
    assert new_author.name == 'Charles Dickens'


    assert new_author.json == {
        "id": new_author.id,
        "name": new_author.name,
        "alive": new_author.alive
    }
