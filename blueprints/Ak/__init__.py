from flask import Blueprint, render_template

people_Ak_bp = Blueprint('people_Ak', __name__,
                              template_folder='templates',
                              static_folder='static', static_url_path='assets')


@people_Ak_bp.route('/')
def index():
    return render_template("templates/timelines.html", padlet="https://padlet.com/jmortensen7/cspcbproject")
