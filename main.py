from flask import Flask, Blueprint, render_template
from blueprints import blueprints_bp
from blueprints.Abhijay import blueprints_Abhijay_bp
from blueprints.Ak import blueprints_Ak_bp
from blueprints.Aiden import blueprints_Aiden_bp
from blueprints.Megan import blueprints_Megan_bp
from blueprints.Zachary import blueprints_Zachary_bp


app = Flask(__name__)
app.register_blueprint(blueprints_bp, url_prefix='/blueprints/repos')
app.register_blueprint(blueprints_Abhijay_bp, url_prefix='/blueprints/Abhijay')
app.register_blueprint(blueprints_Ak_bp, url_prefix='/blueprints/Ak')
app.register_blueprint(blueprints_Aiden_bp, url_prefix='/blueprints/Aiden')
app.register_blueprint(blueprints_Megan_bp, url_prefix='/blueprints/Megan')
app.register_blueprint(blueprints_Zachary_bp, url_prefix='/blueprints/Zachary')


@app.route('/')
def base():
    return render_template("base.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/game')
def game():
    return render_template("game.html")


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True, port="5001")