from application import app # app from __init__.py
from application.books import routes
from application.books import routes_authors
from application import routes
if __name__ == "__main__":
    app.run(debug=True)
