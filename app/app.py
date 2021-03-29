from flask import Flask, Blueprint, render_template

app = Flask(__name__)

test_blueprint = Blueprint('y2021_tri3', __name__, template_folder='templates', static_folder='static',
                           static_url_path='assets')
app.register_blueprint(test_blueprint, url_prefix='/templates')

home_page = Blueprint('home_page', __name__, template_folder='templates', static_folder='static',
                      static_url_path='assets')
app.register_blueprint(home_page, url_prefix='/templates')

about_page = Blueprint('about_page', __name__, template_folder='templates', static_folder='static',
                       static_url_path='assets')
app.register_blueprint(about_page, url_prefix='/templates')

game_page = Blueprint('game_page', __name__, template_folder='templates', static_folder='static',
                       static_url_path='assets')
app.register_blueprint(game_page, url_prefix='templates')


@test_blueprint.route('/pokemon-game')
def display_page(page):
    return render_template('/template/base.html')


@home_page.route('/home')
def display_page(page):
    return render_template('template/home.html')


@about_page.route('/about')
def display_page(page):
    return render_template('template/about.html')


@game_page.route('/game')
def display_page(page):
    return render_template('template/game.html')