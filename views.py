from flask import Flask, render_template
import projects #projects definitions are placed in different file
from example_blueprint import pokemon_game

app = Flask(__name__)
app.register_blueprint(pokemon_game, url_prefix="")

@app.route('/')
def base_route():
    return render_template("base.html", projects=projects.setup())

@app.route('/Mini-lab-storage')
def labstorage_route():
    return render_template("labstorage.html", projects=projects.setup())

if __name__ == "__main__":
    #runs the application on the development server
    app.run(port='5000', host='127.0.0.1', debug = True)