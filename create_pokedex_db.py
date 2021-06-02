from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, inspect
import pprint
import sys

app = Flask(__name__)

''' database setup  '''
dbURI = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

''' table definitions '''


class Pokemon(db.Model):
    Name = db.Column(db.String(255), primary_key=True, nullable=False)
    Type = db.Column(db.String(255), nullable=False)
    Height = db.Column(db.String(255), nullable=False)
    Weight = db.Column(db.Integer, nullable=False)
    Image = db.Column(db.text, nullable=False)


''' table creation '''
db.create_all()