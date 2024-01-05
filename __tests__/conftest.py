import pytest
from application import create_app
from application.books.models import Book

# @pytest.fixture(scope='module')
# def new_book():
#     book = Book(title="Less than Zero", author="Bret Easton Ellis")
#     return book
@pytest.fixture
def client():
    env = "TEST"
    # Initialise a test app
    app = create_app(env)
    
    # Create a test client to which we can make requests
    client = app.test_client()
    


    return client
