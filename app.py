from application import create_app # app from __init__.py
from application.books import routes
from application.authors import routes
from application import routes

if __name__=='__main__':
    app = create_app("PROD")
    app.run(port=5000, debug=True,host="0.0.0.0") 
