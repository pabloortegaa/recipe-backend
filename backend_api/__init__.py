from flask import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Pablo@localhost/test'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Pa$$w0rd1990@jseijas-dbsrv/portega-assignment-db-prod'
db = SQLAlchemy(app)

from backend_api.models import Recipe
from backend_api import routes

db.create_all()

from flask_cors import CORS
CORS(app)





