from pathlib import Path
import json

root_path = Path(__file__).resolve().parent
data_path = root_path.joinpath('data')
trials_path = data_path.joinpath('trials')

def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)