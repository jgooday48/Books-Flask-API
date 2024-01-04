from application import db
from application.books.models import Book
from application.authors.models import Author

db.drop_all()
print("Dropping Database")

db.create_all()
print("Creating Database")

print("Seeding Database")

# entry1 = Book(title="The Hobbit", author="J.R.R Tolkein")
# entry2 = Book(title="American Psycho", author="Bret Easton Ellis")
# entry3 = Book(title="Diary of a Wimpy Kid", author="Jeff Kinney")
# entry4 = Book(title="Harry Potter and the Prisoner of Azkaban", author="J.K Rowling")

# db.session.add(entry1)

# db.session.add_all([entry2, entry3, entry4])

# db.session.commit()

author1 = Author(name="J.K. Rowling")
author2 = Author(name="J.R.R. Tolkein")
author3 = Author(name="Bret Easton Ellis")

db.session.add_all([author1, author2, author3])
db.session.commit()

# Creating a book with a foreign key reference to the author
book1 = Book(title="Harry Potter and the Philosopher's Stone", author_id=author1.id)
book2 = Book(title="Harry Potter and the Chamber of Secrets", author_id=author1.id)
book3 = Book(title="The Hobbit", author_id=author2.id)
book4 = Book(title="The Rules of Atrraction", author_id=author3.id)
db.session.add_all([book1, book2,book3,book4])
db.session.commit()
