from application import db, app
app.app_context().push()

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)

    def __init__(self, title, author_id):
        self.title = title
        self.author_id = author_id

    def __repr__(self):
        return f"Book(id: {self.id}, title: {self.title}, author_id: {self.author_id})"
    
    @property
    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "author_id": self.author_id,
        }
    
# class Author(db.Model):
#     __tablename__ = "authors"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     alive = db.Column(db.Boolean, default=True)  # assuming an "alive" attribute

#     books = db.relationship('Book', backref='author', lazy=True)

#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"Author(id: {self.id}, name: {self.name}, alive: {self.alive})"
    
#     @property
#     def json(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "alive": self.alive,
#         }

