from pathlib import Path
import json

from controllers import Controller


def make_club_players_json():
    """Création du fichier club_players.json s'il n'existe pas.
    """
    folder_path = Path.cwd()/"data"
    file_path = folder_path/"club_players.json"

    if not file_path.exists():
        folder_path.mkdir(parents=True, exist_ok=True)
        file_path.touch()
        with open(file_path, mode="w", encoding="utf-8") as f:
            json.dump([], f)


def make_tournaments_json():
    """Création du fichier tournaments.json s'il n'existe pas.
    """
    folder_path = Path.cwd()/"data"
    file_path = folder_path/"tournaments.json"

    if not file_path.exists():
        folder_path.mkdir(parents=True, exist_ok=True)
        file_path.touch()
        with open(file_path, mode="w", encoding="utf-8") as f:
            json.dump([], f)


make_club_players_json()
make_tournaments_json()
Controller.run()


if __name__ == "__main__":
    """Tests"""
