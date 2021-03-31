from flask import Flask, Blueprint, render_template
from people import people_bp
from people.prep import people_prep_bp
from people.Abhijay import people_Abhijay_bp
from people.Ak import people_Ak_bp
from people.Aiden import people_Aiden_bp
from people.Megan import people_Megan_bp
from people.Zachary import people_Zachary_bp


app = Flask(__name__)
app.register_blueprint(people_bp, url_prefix='/people/repos')
app.register_blueprint(people_prep_bp, url_prefix='/people/prep')
app.register_blueprint(people_Abhijay_bp, url_prefix='/people/Abhijay')
app.register_blueprint(people_Ak_bp, url_prefix='/people/Ak')
app.register_blueprint(people_Aiden_bp, url_prefix='/people/Aiden')
app.register_blueprint(people_Megan_bp, url_prefix='/people/Megan')
app.register_blueprint(people_Zachary_bp, url_prefix='/people/Zachary')


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
    # runs the application on the repl development server
    app.run(debug=True, port="5001")