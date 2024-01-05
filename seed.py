from application import create_app, db
from application.books.models import Book
from application.authors.models import Author

app = create_app()
app.app_context().push()  # push the app context

db.drop_all()
print("Dropping Database")

db.create_all()
print("Creating Database")

print("Seeding Database")


author1 = Author(name="J.K. Rowling")
author2 = Author(name="J.R.R. Tolkein")
author3 = Author(name="Bret Easton Ellis")
author4 = Author(name="Jeff Kinney")

db.session.add_all([author1, author2, author3, author4])
db.session.commit()

# Creating a book with a foreign key reference to the author
book1 = Book(title="Harry Potter and the Philosopher's Stone", author_id=author1.id, genre="fantasy")
book2 = Book(title="Harry Potter and the Chamber of Secrets", author_id=author1.id, genre="fantasy")
book3 = Book(title="The Hobbit", author_id=author2.id, genre="fantasy")
book4 = Book(title="The Rules of Atrraction", author_id=author3.id, genre="black comedy")
book5 = Book(title="Less Than Zero", author_id=author3.id, genre="literary fiction")
book6 = Book(title="American Psycho", author_id=author3.id, genre="postmodern")
book7 = Book(title="Glamorama", author_id=author3.id, genre="satire")
book8 = Book(title="Harry Potter and the Prisoner of Azkaban", author_id=author1.id, genre="fantasy")
book9 = Book(title="Harry Potter and the Goblet of Fire", author_id=author1.id, genre="fantasy")
book10 = Book(title="Harry Potter and the Order of the Phoneix", author_id=author1.id, genre="fantasy")
book11 = Book(title="Harry Potter and the Half Blood Prince", author_id=author1.id, genre="fantasy")
book12 = Book(title="Harry Potter and the Deathly Hallows", author_id=author1.id, genre="fantasy")
book13 = Book(title="Diary of a Wimpy Kid", author_id=author4.id, genre="comedy")
book14 = Book(title="Diary of a Wimpy Kid: Roderick Rules", author_id=author4.id, genre="comedy")
db.session.add_all([book1, book2, book3, book4, book5, book6, book7, book8, book9, book10, book11, book12, book13, book14])
db.session.commit()
