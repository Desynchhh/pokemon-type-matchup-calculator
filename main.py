import os, json

TYPE_CHART_TEMPLATE = {"normal": 1,"fire": 1,"water": 1, "electric": 1,"grass": 1,"ice": 1,"fighting": 1,"poison": 1, "ground": 1, "flying": 1, "psychic": 1, "bug": 1, "rock": 1, "ghost": 1, "dragon": 1, "dark": 1, "steel": 1, "fairy": 1}

CWD = os.getcwd()
CHARTS_DIR = 'pkmn-type-charts'
WEAKNESS_FILE_NAME = 'weaknesses.json'
STRENGTHS_FILE_NAME = 'strengths.json'

PATH_TO_WEAKNESSES_FILE = os.path.join(CWD, CHARTS_DIR, WEAKNESS_FILE_NAME)
PATH_TO_STRENGTHS_FILE = os.path.join(CWD, CHARTS_DIR, STRENGTHS_FILE_NAME)


my_type = {'types': ['fire', 'flying']}


def get_weakness_chart(pkmn_type:str) -> dict:
    with open (PATH_TO_WEAKNESSES_FILE, 'r') as file:
        data = json.loads(file.read())
    if pkmn_type not in data:
        print(f'"{pkmn_type}" is not a pokemon type')
        return
    return data[pkmn_type]




def run():
    pkmn_weakness_chart = TYPE_CHART_TEMPLATE
    for pkmn_type in my_type['types']:
        weakness_chart = get_weakness_chart(pkmn_type)
        for weakness_type in weakness_chart:
            pkmn_weakness_chart[weakness_type] = pkmn_weakness_chart[weakness_type] * weakness_chart[weakness_type]
    results = {
        "quadEffective": [weakness_type for weakness_type in pkmn_weakness_chart if pkmn_weakness_chart[weakness_type] == 4],
        "doubleEffective": [weakness_type for weakness_type in pkmn_weakness_chart if pkmn_weakness_chart[weakness_type] == 2],
        "neutral": [weakness_type for weakness_type in pkmn_weakness_chart if pkmn_weakness_chart[weakness_type] == 1],
        "doubleWeak": [weakness_type for weakness_type in pkmn_weakness_chart if pkmn_weakness_chart[weakness_type] == 0.5],
        "quadWeak": [weakness_type for weakness_type in pkmn_weakness_chart if pkmn_weakness_chart[weakness_type] == 0.25]
    }
    print(json.dumps(results, indent=4))


if __name__ == '__main__':
    run()
