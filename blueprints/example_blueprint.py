from flask import Flask, Blueprint, render_template

pokemon_game = Blueprint('pokemon_game', __name__, template_folder='templates')

@pokemon_game.route("/Mini-lab-storage")

def Minilabstorage():
    return render_template("labstorage.html")

