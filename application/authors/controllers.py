from flask import jsonify, request
from werkzeug import exceptions
from .models import Author
from .. import db

def index(): #show all books
    authors = Author.query.all()

    try:
        return jsonify({"data": [a.json for a in authors ]})
    except:
        raise exceptions.InternalServerError(f"We are working on it")
    
def show(id):
    author = Author.query.filter_by(id=id).first()
    try:
        return jsonify({"data": author.json}), 200
    except:
        raise exceptions.NotFound(f"oh no")
    
def create():
    try:
        data = request.get_json()
        name = data.get('name')
        new_author = Author(name=name)
        db.session.add(new_author)

        db.session.commit()

        return jsonify({ "data": new_author.json}), 201
    except:
        raise exceptions.BadRequest(f"error")

def update(id):
    data = request.json
    author = Author.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
        if hasattr(author, attribute):
            setattr(author, attribute, value)
    db.session.commit()
    return jsonify({ "data":author.json})


def destroy(id):
    author = Author.query.filter_by(id=id).first()
    db.session.delete(author)
    db.session.commit()
    return "author deleted", 204
    
