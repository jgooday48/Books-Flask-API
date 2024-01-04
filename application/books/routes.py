from flask import request
from werkzeug import exceptions
from application import app # app from __init__.
from .controllers import index #, create, show, update, destroy


@app.route('/books', methods=["GET"])
def handle_books():
    #if request.method == "POST": return create()
    if request.method == "GET": return index()

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return { "error": f"Oops {err}"}, 404


@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return { "error": f"Oops {err} "}, 500


@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return { "error": f"Oops {err}" }, 400
