from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, inspect
import pprint
import sys

app = Flask(__name__)

''' database setup  '''
dbURI = 'sqlite:///pokemon.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

''' table definitions '''


class Pokemon(db.Model):
    name = db.Column(db.String(255), primary_key=True, nullable=False)
    type = db.Column(db.String(255), nullable=False)
    height = db.Column(db.String(255), nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    image = db.Column(db.Text, nullable=False)

def addPokemon(Name, Type, Height, Weight, Image):
    pokemon = Pokemon.query.filter_by(name=Name).first()
    print(pokemon)
    #return User.query.get(int(user_id))
    if pokemon and pokemon.name == Name:
        #print("Updating data for User " + player.accountId + " with data " + gameId_list)
        pokemon.type = Type
        pokemon.height = Height
        pokemon.weight = Weight
        pokemon.image = Image
        db.session.commit()

    else:
        new_pokemon = Pokemon(name=Name, type=Type, height=Height, weight=Weight, image=Image)
        #print("Adding New User: " + new_player.accountId + " with data:" + gameId_list)
        db.session.add(new_pokemon)
        db.session.commit()

''' table creation '''
db.create_all()

''' inspect table '''
engine = create_engine(dbURI)
insp = inspect(engine)
for name in insp.get_table_names():
    print("Table " + str(name))