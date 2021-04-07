from flask import Blueprint, render_template

people_aiden_bp = Blueprint('people_aiden', __name__,
                              template_folder='aiden',
                              static_folder='static', static_url_path='assets')


@people_aiden_bp.route('/')
def index():
    return render_template("randomcolorpicker.html")
