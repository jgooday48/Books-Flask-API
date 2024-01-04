from application.books.models import Book
from application import create_app, db
import os

def test_home_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    # Create a test Flask application instance with TESTING set to True
    app = create_app()
    app.config["TESTING"] = True

    # Use the test client provided by Flask
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
