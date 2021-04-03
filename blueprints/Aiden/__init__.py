from flask import Blueprint, render_template

people_Aiden_bp = Blueprint('people_Aiden', __name__,
                              template_folder='templates',
                              static_folder='static', static_url_path='assets')


@people_Aiden_bp.route('/')
def index():
    return render_template("course/timelines.html", padlet="https://padlet.com/jmortensen7/cspcbproject")


def blueprints_Aiden_bp():
    return None