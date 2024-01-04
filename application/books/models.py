from application import db, app

app.app_context().push()

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book(id: {self.id}, title: {self.title})"
    
    @property
    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
        }
