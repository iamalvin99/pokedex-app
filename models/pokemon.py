import sqlite3
import pandas as pd

class POKEMON():
    def getWeakness(pokemonType1, pokemonType2):
        weaknesses = []

        if pokemonType1 == 'Normal' or pokemonType2 == 'Normal':
            weaknesses += ['Fighting']
        if pokemonType1 == 'Fire' or pokemonType2 == 'Fire':
            weaknesses += ['Water', 'Ground', 'Rock']
        if pokemonType1 == 'Water' or pokemonType2 == 'Water':
            weaknesses += ['Grass', 'Electric']
        if pokemonType1 == 'Grass' or pokemonType2 == 'Grass':
            weaknesses += ['Fire', 'Ice', 'Poison', 'Flying', 'Bug']
        if pokemonType1 == 'Electric' or pokemonType2 == 'Electric':
            weaknesses += ['Ground']
        if pokemonType1 == 'Ice' or pokemonType2 == 'Ice':
            weaknesses += ['Fire', 'Fighting', 'Rock', 'Steel']
        if pokemonType1 == 'Fighting' or pokemonType2 == 'Fighting':
            weaknesses += ['Flying', 'Psychic', 'Fairy']
        if pokemonType1 == 'Poison' or pokemonType2 == 'Poison':
            weaknesses += ['Ground', 'Psychic']
        if pokemonType1 == 'Ground' or pokemonType2 == 'Ground':
            weaknesses += ['Water', 'Grass', 'Ice']
        if pokemonType1 == 'Flying' or pokemonType2 == 'Flying':
            weaknesses += ['Electric', 'Ice', 'Rock']
        if pokemonType1 == 'Psychic' or pokemonType2 == 'Psychic':
            weaknesses += ['Bug', 'Ghost', 'Dark']
        if pokemonType1 == 'Bug' or pokemonType2 == 'Bug':
            weaknesses += ['Flying', 'Rock', 'Fire']
        if pokemonType1 == 'Rock' or pokemonType2 == 'Rock':
            weaknesses += ['Water', 'Grass', 'Fighting', 'Ground', 'Steel']
        if pokemonType1 == 'Ghost' or pokemonType2 == 'Ghost':
            weaknesses += ['Ghost', 'Dark']
        if pokemonType1 == 'Dragon' or pokemonType2 == 'Dragon':
            weaknesses += ['Ice', 'Dragon', 'Fairy']
        if pokemonType1 == 'Dark' or pokemonType2 == 'Dark':
            weaknesses += ['Fighting', 'Bug', 'Fairy']
        if pokemonType1 == 'Steel' or pokemonType2 == 'Steel':
            weaknesses += ['Fire', 'Fighting', 'Ground']
        if pokemonType1 == 'Fairy' or pokemonType2 == 'Fairy':
            weaknesses += ['Poison', 'Steel']

        return weaknesses

    def addWeakness(list):
        for pokemon in list:
            weaknessText = ''
            weaknesses = POKEMON.getWeakness(pokemon[3], pokemon[4])
            weaknessText = ':'.join(weaknesses)
            pokemon.append(weaknessText)
        return list

    def getResistance(pokemonType1, pokemonType2):
        resistances = []
        immunity = []

        if pokemonType1 == 'Normal' or pokemonType2 == 'Normal':
            resistances += ['N/A']
            immunity += ['Ghost']
        if pokemonType1 == 'Fire' or pokemonType2 == 'Fire':
            resistances += ['Fire', 'Grass', 'Ice', 'Bug', 'Steel', 'Fairy']
            immunity += ['N/A']
        if pokemonType1 == 'Water' or pokemonType2 == 'Water':
            resistances += ['Fire', 'Water', 'Ice', 'Steel']
            immunity += ['N/A']
        if pokemonType1 == 'Grass' or pokemonType2 == 'Grass':
            resistances += ['Water', 'Electric', 'Grass', 'Ground']
            immunity += ['N/A']
        if pokemonType1 == 'Electric' or pokemonType2 == 'Electric':
            resistances += ['Electric', 'Flying', 'Steel']
            immunity += ['N/A']
        if pokemonType1 == 'Ice' or pokemonType2 == 'Ice':
            resistances += ['Ice']
            immunity += ['N/A']
        if pokemonType1 == 'Fighting' or pokemonType2 == 'Fighting':
            resistances += ['Bug', 'Rock', 'Dark']
            immunity += ['N/A']
        if pokemonType1 == 'Poison' or pokemonType2 == 'Poison':
            resistances += ['Grass', 'Fighting', 'Poison', 'Bug', 'Fairy']
            immunity += ['N/A']
        if pokemonType1 == 'Ground' or pokemonType2 == 'Ground':
            resistances += ['Poison', 'Rock']
            immunity += ['Electric']
        if pokemonType1 == 'Flying' or pokemonType2 == 'Flying':
            resistances += ['Grass', 'Fighting', 'Bug']
            immunity += ['Ground']
        if pokemonType1 == 'Psychic' or pokemonType2 == 'Psychic':
            resistances += ['Fighting', 'Psychic']
            immunity += ['N/A']
        if pokemonType1 == 'Bug' or pokemonType2 == 'Bug':
            resistances += ['Grass', 'Fighting', 'Ground']
            immunity += ['N/A']
        if pokemonType1 == 'Rock' or pokemonType2 == 'Rock':
            resistances += ['Normal', 'Fire', 'Poison', 'Flying']
            immunity += ['N/A']
        if pokemonType1 == 'Ghost' or pokemonType2 == 'Ghost':
            resistances += ['Poison', 'Bug']
            immunity += ['Normal', 'Fighting']
        if pokemonType1 == 'Dragon' or pokemonType2 == 'Dragon':
            resistances += ['Fire', 'Water', 'Grass', 'Electric']
            immunity += ['N/A']
        if pokemonType1 == 'Dark' or pokemonType2 == 'Dark':
            resistances += ['Ghost', 'Dark']
            immunity += ['Psychic']
        if pokemonType1 == 'Steel' or pokemonType2 == 'Steel':
            resistances += ['Normal', 'Grass', 'Ice', 'Flying', 'Psychic', 'Bug', 'Rock', 'Dragon', 'Steel', 'Fairy']
            immunity += ['Poison']
        if pokemonType1 == 'Fairy' or pokemonType2 == 'Fairy':
            resistances += ['Fighting', 'Bug', 'Dark']
            immunity += ['Dragon']

        return resistances, immunity
        

    def addResistances(list):
        for pokemon in list:
            resistanceText = ''
            immunityText = ''

            resistances, immunity = POKEMON.getResistance(pokemon[3], pokemon[4])
           
            resistanceText = ':'.join(resistances)
            immunityText = ':'.join(immunity)

            pokemon.append(resistanceText)
            pokemon.append(immunityText)
        return list

    def check_exist():
        try:
            conn = sqlite3.connect('pokemons.sqlite')
            cur = conn.cursor()

            result = cur.execute('''SELECT * FROM pokemon''').fetchone()

            conn.close()

            if result:
                return True
        except sqlite3.OperationalError as e:
            return False

    def database(pokeList):
        conn = sqlite3.connect('pokemons.sqlite')
        cur = conn.cursor()

        df = pd.DataFrame(pokeList, columns=['index', 'name', 'type1', 'type2', 'url', 'imageurl', 'weakness', 'resistance', 'immunity'])
        cur.execute('''CREATE TABLE IF NOT EXISTS pokemon ([index] INTEGER, [name] TEXT, [type1] TEXT, [type2] TEXT, [url] TEXT, [image] TEXT, [weakness] TEXT, [resistance] TEXT, [immunity] TEXT)''')
        df.to_sql('pokemon', conn, if_exists='replace', index = False)

        conn.close()
      

    def search_pokemon(name):
        conn = sqlite3.connect('pokemons.sqlite')
        cur = conn.cursor()

        search = f"SELECT * FROM pokemon WHERE name LIKE '%{name}%'"
        results = cur.execute(search).fetchall()

        conn.close()
        return results
    
    @staticmethod    
    def getAllPOKEMONs():
        POKEMONs = list(POKEMON.objects())
        return sorted(POKEMONs, key=lambda pokemon: pokemon.index)
