import json
import os

CHAMPIONS_DIR = os.path.join(os.path.dirname(__file__), '../data/champions')
CHAMPIONS_LIST_PATH = os.path.join(os.path.dirname(__file__), '../data/champions.json')

class ChampionsService():
    
    def get_all_champions(cls):
        with open(CHAMPIONS_LIST_PATH, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            champions = json_data["data"]
        return champions
        

    def get_champion_by_name(cls, name: str):
        file_path = os.path.join(CHAMPIONS_DIR, f"{name}.json")
        if not os.path.isfile(file_path):
            raise Exception("Champion not found")
        with open(file_path, 'r', encoding='utf-8') as f:
            champion = json.load(f)
        return champion