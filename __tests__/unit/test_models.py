from application.books.models import Book

def test_new_post_with_fixture(new_book):
    """
    GIVEN a Post model
    WHEN a new Post is created
    THEN check the title and content fields are defined correctly
    """
    assert new_book.title == 'Less than Zero'
    assert new_book.author == 'Bret Easton Ellis'

    assert new_book.json == {
        "id": new_book.id,
        "title": new_book.title,
        "author": new_book.author,
    }
