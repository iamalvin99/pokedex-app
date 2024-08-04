from flask import Flask, render_template, request, jsonify
from controllers.pokedex import pokedex
from models.pokemon import POKEMON

def create_app():
    app = Flask(__name__)

    app.static_folder = 'assets'
 
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    return app

app = create_app()

app.register_blueprint(pokedex)

# @app.route('/')
# def show_pokemon():
#     return render_template('base.html')