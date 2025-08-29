from fastapi import APIRouter, HTTPException
import os
import json

router = APIRouter()

CHAMPIONS_DIR = os.path.join(os.path.dirname(__file__), '../data/champions')
CHAMPIONS_LIST_PATH = os.path.join(os.path.dirname(__file__), '../data/champions.json')

@router.get("/champions")
def get_all_champions():
    try:
        with open(CHAMPIONS_LIST_PATH, 'r', encoding='utf-8') as f:
            champions = json.load(f)
        return champions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/champions/{name}")
def get_champion_by_name(name: str):
    file_path = os.path.join(CHAMPIONS_DIR, f"{name}.json")
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="Champion not found")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            champion = json.load(f)
        return champion
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
