from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '224d3250278e0d4193cca92fe7b644a4cd71afcd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loan.db'
db = SQLAlchemy(app)

from loan import routes
