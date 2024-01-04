from application import db
from application.books.models import Book

db.drop_all()
print("Dropping Database")

db.create_all()
print("Creating Database")

print("Seeding Database")

entry1 = Book(title="The Hobbit", author="J.R.R Tolkein")
entry2 = Book(title="American Psycho", author="Bret Easton Ellis")
entry3 = Book(title="Diary of a Wimpy Kid", author="Jeff Kinney")
entry4 = Book(title="Harry Potter and the Prisoner of Azkaban", author="J.K Rowling")

db.session.add(entry1)

db.session.add_all([entry2, entry3, entry4])

db.session.commit()
