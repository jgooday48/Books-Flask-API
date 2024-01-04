from flask import jsonify, request
from werkzeug import exceptions
from .models import Book
from .. import db

def index(): #show all books
    books = Book.query.all()

    try:
        return jsonify({"data": [b.json for b in books ]})
    except:
        raise exceptions.InternalServerError(f"We are working on it")
    
def show(id):
    book = Book.query.filter_by(id=id).first()
    try:
        return jsonify({"data": book.json}), 200
    except:
        raise exceptions.NotFound(f"oh no")
    
def create():
    try:
        title, author = request.json.values()

        new_book = Book(title, author)
        db.session.add(new_book)
        db.session.commit()
        return jsonify({ "data": new_book.json}), 201
    except:
        raise exceptions.BadRequest(f"error")

def update(id):
    data = request.json
    book = Book.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(book, attribute):
            setattr(book, attribute, value)
    db.session.commit()
    return jsonify({ "data":book.json})


def destroy(id):
    book = Book.query.filter_by(id=id).first()
    db.session.delete(book)
    db.session.commit()
    return "book deleted", 204
    
