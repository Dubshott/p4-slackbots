from flask import Flask, jsonify, make_response
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

class PokemonTypeRating(db.Model):
    PokemonType_name = db.Column(db.String(255), primary_key=True, nullable=False)
    like_count = db.Column(db.integer, nullable=False)
    dislike_count = db.Column(db.integer, nullable=False)

def addPokemonTypeRating(PokemonType):
    pokemonType_rec = PokemonTypeRating.query.fiter_by(PokemonType_name=PokemonType).first()
    if pokemonType_rec and pokemonType.PokemonType_name == PokemonType:
        return
    else:
        new_pokemonType_rec = PokemonTypeRating(PokemonType_name=PokemonType, like_count=0, dislike_count=0)
        db.session.add(new_pokemonType_rec)
        db.session.commit()

def findPokemonTypeRating(PokemonType):
    pokemonType_rec = PokemonTypeRating.query.fiter_by(PokemonType_name=PokemonType).first()
    if pokemonType_rec and pokemonType_rec.PokemonType_name == PokemonType:
        return pokemonType_rec
    return


def update_like_count(pokemonType_rec):
    pokemonType_rec.like_count++
    db.session.commit()

def update_dislike_count(pokemonType_rec):
    pokemonType_rec.dislike_count++
    db.session.commit()


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

def findPokemon(Name):
    pokemon = Pokemon.query.filter_by(name=Name).first()
    print(pokemon)
    if pokemon and pokemon.name == Name:
        return pokemon
    return

def getPokemon(Name):
    pokemon = Pokemon.query.filter_by(name=Name).first()
    Type, Weight, Height, Image = '', '', '', ''
    if pokemon and pokemon.name == Name:
        Type = pokemon.type
        Height = pokemon.height
        Weight = pokemon.weight
        Image = pokemon.image
    resp = {'name':Name, 'type': Type, 'height':Height, 'weight':Weight, 'image':Image}
    print(resp)
    return resp


''' table creation '''
db.create_all()

''' Enter Data in PokemonTypeRating Table'''
for type in ['Normal', 'Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic',
             'Bug', 'Rock', 'Ghost', 'Dark', 'Dragon', 'Steel', 'Fairy']:
    addPokemonTypeRating(type)

''' inspect table '''
engine = create_engine(dbURI)
insp = inspect(engine)
for name in insp.get_table_names():
    print("Table " + str(name))