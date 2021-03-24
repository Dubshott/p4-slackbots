from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
import projects #projects definitions are placed in different file

app = Flask(__name__)

@app.route('/')
def base_route():
    return render_template("base.html", projects=projects.setup())

if __name__ == "__main__":
    #runs the application on the development server
    app.run(port='5000', host='127.0.0.1', debug = True)