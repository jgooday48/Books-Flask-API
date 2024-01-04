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

class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    alive = db.Column(db.Boolean, default=True)

    def __init__(self, name, alive):
        self.name = name
        self.alive = alive

    def __repr__(self):
        return f"Book(id: {self.id}, title: {self.name})"
    
    @property
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "alive": self.alive,
        }
