from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.secret_key = "Ki34nci34asd99sdaf34iadf9"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from clipmock import routes