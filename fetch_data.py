import os
import json
import requests

# Patch actuel
PATCH = "15.17.1"

# Répertoire racine où stocker les données
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
CHAMPIONS_DIR = os.path.join(DATA_DIR, "champions")

# Création des dossiers si absents
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(CHAMPIONS_DIR, exist_ok=True)


def download_json(url, filepath):
    """Télécharge un JSON et le sauvegarde en local"""
    print(f"⬇️  Téléchargement {url} ...")
    response = requests.get(url)
    response.raise_for_status()
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(response.json(), f, indent=2, ensure_ascii=False)
    print(f"✅ Sauvegardé -> {filepath}")


def fetch_champions():
    """Récupère la liste des champions + fichiers détaillés"""
    champions_url = f"https://ddragon.leagueoflegends.com/cdn/{PATCH}/data/en_US/champion.json"
    champions_path = os.path.join(DATA_DIR, "champions.json")

    # Liste des champions
    response = requests.get(champions_url)
    response.raise_for_status()
    champions_data = response.json()
    with open(champions_path, "w", encoding="utf-8") as f:
        json.dump(champions_data, f, indent=2, ensure_ascii=False)
    print(f"✅ Liste des champions sauvegardée -> {champions_path}")

    # Fichiers détaillés
    for champ_name in champions_data["data"].keys():
        champ_url = f"https://ddragon.leagueoflegends.com/cdn/{PATCH}/data/en_US/champion/{champ_name}.json"
        champ_path = os.path.join(CHAMPIONS_DIR, f"{champ_name}.json")
        download_json(champ_url, champ_path)


def fetch_items():
    """Récupère la liste des items"""
    items_url = f"https://ddragon.leagueoflegends.com/cdn/{PATCH}/data/en_US/item.json"
    items_path = os.path.join(DATA_DIR, "items.json")
    download_json(items_url, items_path)


def fetch_runes():
    """Récupère les runes"""
    runes_url = f"https://ddragon.leagueoflegends.com/cdn/{PATCH}/data/en_US/runesReforged.json"
    runes_path = os.path.join(DATA_DIR, "runes.json")
    download_json(runes_url, runes_path)


def main():
    print("🔄 Récupération des données League of Legends...")
    fetch_champions()
    fetch_items()
    fetch_runes()
    print("\n🎉 Toutes les données sont téléchargées dans le dossier /data !")


if __name__ == "__main__":
    main()
