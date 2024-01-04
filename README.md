# Books-Flask-API

## Instructions
- In the console run `pipenv shell`
- Run `pipenv install` to install the required modules
- `touch .env` to add a database instance
- Set up a postgres SQL db instance on [elephantSQL](https://www.elephantsql.com/)
- Add the following to the .env file:
```
FLASK_DEBUG=1
SQLALCHEMY_DATABASE_URI=
```
- in the elephant sql URI, where it says `postgres`, add `ql` to it so that it now becomes `postgresql`
- make sure that your interpreter is selected as a pipenv one related to your file
- Run `python seed.py` to seed the db instance
- Run `python app.py` to start the api
