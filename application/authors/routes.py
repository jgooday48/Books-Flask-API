from flask import request, Blueprint
from werkzeug import exceptions
from .controllers import index, create, show, update #, destroy

authors = Blueprint("authors", __name__)

@authors.route('/authors', methods=["GET", "POST"])
def handle_authors():
    if request.method == "POST": return create()
    if request.method == "GET": return index()


@authors.route('/authors/<int:id>', methods=["GET", "PATCH", "DELETE"])
def handle_author(id):
    if request.method == "GET": return show(id)
    if request.method == "PATCH": return update(id)
    #if request.method == "DELETE": return destroy(id)


@authors.errorhandler(exceptions.NotFound)
def handle_404(err):
    return { "error": f"Oops {err}"}, 404


@authors.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return { "error": f"Oops {err} "}, 500


@authors.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return { "error": f"Oops {err}" }, 400
