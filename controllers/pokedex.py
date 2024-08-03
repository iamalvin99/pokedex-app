from flask import Blueprint, render_template, request, jsonify
# from app import db
from models.scraper import Scraper
from models.pokemon import POKEMON

import json

pokedex = Blueprint('pokedex', __name__)

@pokedex.route('/pokedex')
def poke():
    exist = POKEMON.check_exist()

    if exist:
        return render_template('showpokemon.html')
    else:
        content = Scraper.scrape_from_site()
        content = POKEMON.addWeakness(content)
        content = POKEMON.addResistances(content)
        POKEMON.database(content)
        return render_template('showpokemon.html')

@pokedex.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    results = POKEMON.search_pokemon(name)
    return jsonify(results)

