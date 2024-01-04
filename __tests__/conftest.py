import pytest
from application import app, db
from application.books.models import Book

@pytest.fixture(scope='module')
def new_book():
    book = Book(title="Less than Zero", author="Bret Easton Ellis")
    return book
