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
    weight = db.Column(db.integer, nullable=False)
    Image_Url = db.Column(db.text, nullable=False)



def addPokemon(AccountId, EncryptedId, gameId_list):
    player = Players.query.filter_by(accountId=AccountId).first()
    print(player)
    #return User.query.get(int(user_id))
    if player and player.accountId == AccountId:
        #print("Updating data for User " + player.accountId + " with data " + gameId_list)
        player.matchListData = gameId_list
        db.session.commit()

    else:
        new_player = Players(accountId=AccountId, encryptedId=EncryptedId, matchListData=gameId_list)
        #print("Adding New User: " + new_player.accountId + " with data:" + gameId_list)
        db.session.add(new_player)
        db.session.commit()

''' table creation '''
db.create_all()

''' inspect table '''
engine = create_engine(dbURI)
insp = inspect(engine)
for name in insp.get_table_names():
    print("Table " + str(name))
