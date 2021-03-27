from flask import Flask, Blueprint, render_template

app = Flask(__name__)
test_blueprint = Blueprint('y2021_tri3', __name__, template_folder='templates', static_folder='static',
                           static_url_path='assets')
app.register_blueprint(test_blueprint, url_prefix='/templates')


@test_blueprint.route('/pokemon-game')
def display_page(page):
    return render_template('/template/base.html')
