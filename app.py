from application import app # app from __init__.py
from application.books import routes
from application.authors import routes
from application import routes
if __name__ == "__main__":
    app.run(debug=True)
