from flask import Flask, render_template
import projects #projects definitions are placed in different file
from blueprints.Abhijay.__init__ import people_Abhijay_bp
from blueprints.Aiden.__init__ import people_Aiden_bp
from blueprints.Ak.__init__ import people_Ak_bp
from blueprints.Megan.__init__ import people_Megan_bp
from blueprints.Zachary.__init__ import people_Zachary_bp

app = Flask(__name__)
app.register_blueprint(people_Abhijay_bp, url_prefix='/abhijay')
app.register_blueprint(people_Aiden_bp, url_prefix='/aiden')
app.register_blueprint(people_Ak_bp, url_prefix='/ak')
app.register_blueprint(people_Megan_bp, url_prefix='/megan')
app.register_blueprint(people_Zachary_bp, url_prefix='/zachary')

@app.route('/')
def base_route():
    return render_template("base.html", projects=projects.setup())

@app.route('/Mini-lab-storage')
def labstorage_route():
    return render_template("labstorage.html", projects=projects.setup())

if __name__ == "__main__":
    #runs the application on the development server
    app.run(port='5000', host='127.0.0.1', debug = True)
