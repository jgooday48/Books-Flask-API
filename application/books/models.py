from application import db
# app.app_context().push()

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    genre = db.Column(db.String(100), nullable=False)

    def __init__(self, title, author_id, genre):
        self.title = title
        self.author_id = author_id
        self.genre = genre

    def __repr__(self):
        return f"Book(id: {self.id}, title: {self.title}, author_id: {self.author_id})"
    
    @property
    def json(self):
        return {
            "id": self.id,
            "author_id": self.author_id,
            "title": self.title,
            "genre": self.genre
        }
    

