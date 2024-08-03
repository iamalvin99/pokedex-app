from flask import render_template, request, jsonify
# from app import app, db
from app import app

from controllers.pokedex import pokedex

app.register_blueprint(pokedex)

from models.pokemon import POKEMON

@app.route('/')
def show_pokemon():
    return render_template('showpokemon.html')

