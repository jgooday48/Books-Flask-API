from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os


db = SQLAlchemy() # initialise db

def create_app(env=None):
    load_dotenv()
    app = Flask(__name__)

    app.json_provider_class.sort_keys = False
    CORS(app)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["SQLALCHEMY_DATABASE_URI"]
    
    db.init_app(app)
    app.app_context().push()

    #import blueprints
    from application.routes import main
    app.register_blueprint(main)

    from application.authors.routes import authors
    app.register_blueprint(authors)

    from application.books.routes import books
    app.register_blueprint(books)

    return app

