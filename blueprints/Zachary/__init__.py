from flask import Blueprint, render_template

people_Zachary_bp = Blueprint('people_Zachary', __name__,
                              template_folder='Zachary',
                              static_folder='static', static_url_path='assets')


@people_Zachary_bp.route('/')
def index():
    return render_template("randomjokegenerator.html")