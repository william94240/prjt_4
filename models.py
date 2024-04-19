from datetime import datetime
from pathlib import Path
import json
import os

from views import View


class Player:
    """
    Le joueur.
    """

    def __init__(self, first_name: str, last_name: str, chess_id: str, birthday: datetime):
        """Création du joueur.
        Args:
            nom (str): le nom du joueur à créer.
            prenom (str): le prenom du joueur à créer.
            date_naissance (datetime): la date_naissance du joueur à créer.
            identifiant_echecs (str): l'identifiant nationale d'echecs
            du joueur à créer.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.chess_id = chess_id
        self.birthday = birthday

        # Initialiser les points du joueur à 0
        # self.points = 0.0

    def __repr__(self) -> str:
        """Méthode pour afficher les détails du joueur

        Returns:
            str: affiche les details sur le joueur.
        """

        return f"{'first_name': {self.first_name}, 'last_name': {self.last_name}, 'chess_id': {self.chess_id}, 'birthday': {self.birthday}}"

    def __str__(self) -> str:
        """Méthode pour afficher les détails du joueur

        Returns:
            str: affiche les details sur le joueur.
        """

        return f" Prénom: {self.first_name}\n Nom: {self.last_name}\n Identifiant echecs: {self.chess_id}\n Date de naissance: {self.birthday}\n"

    def player_serialize(self):
        """
        Transforme les données en dictionnaire

        Returns:
            Dict: données en Dictionnaire
        """

        player_serialized = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "chess_id": self.chess_id,
            "birthday": self.birthday.strftime("%Y-%m-%d"),

        }

        return player_serialized

    def save_player(self):
        """Sauvegarde le joueur dans un fichier json.

        Returns:
            _type_: _description_
        """

        file_path = Path.cwd()
        file_path = file_path/"data"
        file_path = file_path/"players.json"

        if not os.path.exists(file_path):
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.touch()
            with open(file_path, "w") as f:
                json.dump([], f)

        with open(file_path, "r+", encoding="utf-8") as f:
            players = json.load(f)
            print(players)
            player_serialized = self.player_serialize()
            print(player_serialized)

            players.append(player_serialized)
            print(players)

            json.dump(players, f, indent=4)


class Tournament:

    """Le tournoi.
    """
    # Liste des tournois.
    tournaments = []
    # Liste pour stocker les joueurs inscrits au tournoi.
    players_registered_in_tournement = []

    def __init__(self, name_tournament: str, location: str, start_date: datetime, end_date: datetime,
                 nb_round: int = 4, description: str = ""):
        """Creation Tournoi.
    # NB: DOTO ajouter nb players.
        Args:
            name_tournament (str): Le nom du tournoi
            location (str): Le lieu du tournoi
            start_date (datetime): La date de début du tournoi
            end_date (datetime): La date de fin du tournoi
            nb_round (int, optional): Le nombre de tours du tournoi. Defaults to 4.
            description (str, optional): La description du tournoi. Defaults to "".
        """
        self.name_tournament = name_tournament
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.nb_round = nb_round
        self.description = description
        self.rounds = []

        # le numéro correspondant au tour .
        number_of_round = len(self.rounds) + 1

    def __repr__(self):
        """Méthode pour afficher les détails sur tournoi

        Returns:
            str: affiche les details sur le joueur.
        """

        return f'{"name_tournament": {self.name_tournament}, "location": {self.location}, "start_date": {self.start_date}, "end_date": {self.end_date}, "nb_round": {self.nb_round}, "description": {self.description}}'

    def __str__(self):
        """
        Méthode pour afficher les détails sur tournoi
        """

        return f"Nom du tournoi: {self.name_tournament}\n Lieu: {self.location}\n Date début: {self.start_date}\n Date fin: {self.end_date}\n Nombre de Tours: {self.nb_round}\n Description: {self.description}"

    def tournament_serialize(self):
        """
        Transforme les données en dictionnaire

        Returns:
            Dict: données sous forme de Dictionnaire
        """

        tournament_serialized = {
            "name_tournament": self.name_tournament,
            "location": self.location,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "nb_round": self.nb_round,
            "description": self.description
        }

        return tournament_serialized

    def save_tournament(self):
        """Sauvegarde le tounoi dans un fichier tournaments.json.

        Returns:
            _type_: _description_

        """

        file_path = Path.cwd()
        file_path = file_path/"data"
        file_path = file_path/"tournaments.json"

        if not os.path.exists(file_path):
            file_path.parent.mkdir(exist_ok=True)
            file_path.touch()
            with open(file_path, "w") as f:
                json.dump([], f)

        with open(file_path, "r+", encoding="utf-8") as f:
            tournaments = json.load(f)
            print(tournaments)
            tournament_serialized = self.tournament_serialize()
            print(tournament_serialized)

            tournaments.append(tournament_serialized)
            print(tournaments)

            # json.dump(tournaments, f, indent=4)


class Match:
    """
    Le Match.
    """

    def __init__(self, player_1: Player, player_2: Player, score_player_1: int = 0,  score_player_2: int = 0):
        """Création de l'entité Match.

        Args:
            player_1 (Joueur): Le premier joueur.
            player_2 (Joueur): Le second  joueur.
        """
        self.player_1 = player_1
        self.player_2 = player_2
        # Peut être rédefinit plus tard lors de la saisie des résultats
        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2

    def definir_resultat(self, score_player_1: int = 0, score_player_2: int = 0):
        """
        Méthode pour définir le résultat du match

        Args:
            resultat (Tuple): Le resultat
        """
        self.resultat = (score_player_1, score_player_2)

    def obtenir_resultat(self):
        """
        Méthode pour obtenir les résultats du match

        Returns:
            str: Retour des points de deux joueurs.
        """

        return self.resultat

    def __str__(self):
        """
        Méthode pour afficher les détails du match
        """
        return f"Joueur 1: {self.player_1} - point: {self.score_player_1} ::: Joueur 2: {self.player_2} - point: {self.score_player_2}"


class Round:
    """ Création de l'entité Round."""

    def __init__(self, round_name: str, start_datetime: datetime, end_datetime: datetime):
        self.round_name = round_name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.matches = []

    def set_round(self):
        """Returne round info en liste"""
        return [self.round_name, self.start_datetime, self.end_datetime, self.matches]

    def get_match_pairing(self, player_1, player_2):
        """Set match paring as tuple"""
        match = (
            f"{player_1['last_name']}, {player_1['first_name']}",
            player_1["score"],
            f"{player_2['last_name']}, {player_2['first_name']}",
            player_2["score"]
        )
        self.matches.append(match)


if __name__ == "__main__":
    """
    Tests
    """

    # player1 = Player("William", "Mopete", "AB12345", datetime(1962, 4, 14))
    # print(player1)
    # # print(player1.get_player_in_dictionnary_format())
    # player1.save_player()

    # player2 = Player("Nelly", "Mopete", "AB98745", datetime(1964, 6, 2))
    # print(player2)
    # # print(player2.get_player_in_dictionnary_format())
    # player2.save_player()

    tournament_1 = Tournament("Lipopo", "Kinshasa", datetime(
        2024, 4, 18), datetime(2024, 4, 18), 4, "ras")
    print(tournament_1)
    tournament_1.save_tournament()
