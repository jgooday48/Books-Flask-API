from application import app
from flask import jsonify

@app.route('/')
def hello():
    return jsonify({
        "message": "Welcome",
        "description": "Books API",
        "endpoints": [
            "GET /",
            "GET /books"
        ]
    }), 200
