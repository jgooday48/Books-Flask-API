from application import app
from flask import jsonify

@app.route('/')
def hello():
    return jsonify({
        "message": "Welcome",
        "description": "Books API",
        "endpoints": [
            "GET /",
            "GET /books",
            "GET /books/<int:id>",
            "POST /books",
            "PATCH /books/<int:id>",
            "DELETE /books/<int:id>"
        ]
    }), 200
