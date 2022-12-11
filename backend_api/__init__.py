from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Pablo@localhost/postgres'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Pa$$w0rd1990@PabloOrtega-srv/portega-assignment-dev-db'
db = SQLAlchemy(app)

from backend_api.models import Recipe
from backend_api import routes

db.create_all()

from flask_cors import CORS
CORS(app)









