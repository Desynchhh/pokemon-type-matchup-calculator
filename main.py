import json, pkmn_calculator
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/<pkmn_types>')
def index(pkmn_types):
    pkmn_types = {'types': pkmn_types.split('_')}
    print(pkmn_types)
    # return jsonify(pkmn_types)
    return jsonify(pkmn_calculator.run(pkmn_types))
app.run()