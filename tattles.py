import json


def get_tattle(enemy: str) -> str:
    with open(f'tattle_data/{enemy}.json', 'r') as enemy_data:
        data = json.load(enemy_data)

    return format_tattle(data)


def format_tattle(d) -> str:
    return d["name"]
    # should probably get another function going that builds the string out the way i want it
    # maybe even bring this all to a new file eventually???

