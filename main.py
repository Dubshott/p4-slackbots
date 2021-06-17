from flask import Flask, Blueprint, render_template

"""
from blueprints import blueprints_bp
from blueprints.Abhijay import blueprints_Abhijay_bp
from blueprints.Ak import blueprints_Ak_bp
from blueprints.Aiden import blueprints_Aiden_bp
from blueprints.Megan import blueprints_Megan_bp
from blueprints.Zachary import blueprints_Zachary_bp
"""
"""

app.register_blueprint(blueprints_bp, url_prefix='/blueprints/repos')
app.register_blueprint(blueprints_Abhijay_bp, url_prefix='/blueprints/Abhijay')
app.register_blueprint(blueprints_Ak_bp, url_prefix='/blueprints/Ak')
app.register_blueprint(blueprints_Aiden_bp, url_prefix='/blueprints/Aiden')
app.register_blueprint(blueprints_Megan_bp, url_prefix='/blueprints/Megan')
app.register_blueprint(blueprints_Zachary_bp, url_prefix='/blueprints/Zachary')
"""
app = Flask(__name__)

@app.route('/')
def base():
    return render_template("base.html")

@app.route('/base')
def base_return():
    return render_template("base.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/game')
def game():
    return render_template("game.html")

@app.route('/pokedex')
def pokedex():
    return render_template("pokedex.html")
@app.route('/login')
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True, port="5001")
    #hi
    #bruh