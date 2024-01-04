from application import db, app
app.app_context().push()

class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    alive = db.Column(db.Boolean, default=True)  # assuming an "alive" attribute

    books = db.relationship('Book', backref='author', lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Author(id: {self.id}, name: {self.name}, alive: {self.alive})"
    
    @property
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "alive": self.alive,
        }

