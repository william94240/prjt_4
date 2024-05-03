from datetime import datetime, date
from pathlib import Path
import json
import os

from views import View


class Player:
    """
    Le joueur.
    """

    def __init__(self, first_name: str, last_name: str, chess_id: str, birthday: date):
        """Création du joueur.
        Args:
            last_name (str): le nom du joueur à créer.
            first_name (str): le prenom du joueur à créer.
            birthday (datetime): la date_naissance du joueur à créer.
            chess_id (str): l'identifiant nationale d'echecs du joueur à créer.
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
            Dict: retourne des données sous la forme d'un dictionnaire
        """

        player_serialized = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "chess_id": self.chess_id,
            "birthday": self.birthday.strftime("%Y-%m-%d"),

        }

        return player_serialized

    def save_club_player(self):
        """Sauvegarde le joueur dans un fichier json.

        Returns:
            _type_: None
        """

        folder_path = Path.cwd()/"data"
        file_path = folder_path/"club_players.json"

        if not os.path.exists(file_path):
            folder_path.mkdir(parents=True, exist_ok=True)
            file_path.touch()
            with open(file_path, "w") as f:
                json.dump([], f)

        with open(file_path, "r", encoding="utf-8") as f:
            players = json.load(f)

        player_serialized = self.player_serialize()
        players.append(player_serialized)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(players, f, indent=4)

    @classmethod
    def player_deserialize(cls, player_serialized):
        """
        Restaure le dictionnaire en données originales.
        """

        player_serialized["birthday"] = date.fromisoformat(
            player_serialized["birthday"])

        player = cls(player_serialized["first_name"], player_serialized["last_name"],
                     player_serialized["chess_id"], player_serialized["birthday"])

        return player

    @classmethod
    def display_club_players(cls):
        """Affiche les joueurs inscrits au club.
        """

        file_path = Path.cwd()/"data"/"club_players.json"

        with open(file_path, "r", encoding="utf-8") as f:
            players_serialized = json.load(f)
            players = []
            # [cls.player_deserialize(
            #     player_serialized) for player_serialized in players_serialized]

            for player_serialized in players_serialized:
                player = cls.player_deserialize(player_serialized)
                players.append(player.__str__())

        return players


class Tournament:

    """Le tournoi.
    """
    # Liste des tournois.
    tournaments = []
    # Liste pour stocker les joueurs inscrits au tournoi.
    # players = []

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
        self.players = []

    def __repr__(self):
        """Méthode pour afficher les détails sur tournoi

        Returns:
            str: affiche les details sur le joueur.
        """

        return f'{"Nom du tournoi": {self.name_tournament}, "Lieu": {self.location}, "Date début": {self.start_date}, "Date fin": {self.end_date}, "Nombre de Tours": {self.nb_round}, "Description": {self.description}}'

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
            "Nom du tournoi": self.name_tournament,
            "Lieu": self.location,
            "Date début": self.start_date.strftime("%Y-%m-%d"),
            "Date fin": self.end_date.strftime("%Y-%m-%d"),
            "Nombre de Tours": self.nb_round,
            "Description": self.description,
            "Joueurs": self.players

        }

        tournament_serialized["Joueurs"] = [
            player.player_serialize() for player in self.players]

        return tournament_serialized

    def save_tournament(self):
        """Sauvegarde le tounoi dans un fichier tournaments.json.

        Returns:
            _type_: _description_

        """

        folder_path = Path.cwd()/"data"
        file_path = folder_path/"tournaments.json"

        if not os.path.exists(file_path):
            folder_path.mkdir(exist_ok=True)
            file_path.touch()
            with open(file_path, "w") as f:
                json.dump([], f)

        with open(file_path, "r", encoding="utf-8") as f:
            tournaments = json.load(f)
            tournament_serialized = self.tournament_serialize()
            tournaments.append(tournament_serialized)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(tournaments, f, indent=4)

    def add_tournament_player(self, player: Player):
        """Sauvegarde le joueur dans le fichier tournament.

        Returns:
            _type_: _description_

        """
        self.players.append(player)
        return self.players

    @classmethod
    def tournament_deserialize(cls, tournament_serialized):
        """
        Restaure le dictionnaire en données originales.
        """

        tournament_serialized["start_date"] = date.fromisoformat(
            tournament_serialized["start_date"])
        tournament_serialized["end_date"] = date.fromisoformat(
            tournament_serialized["end_date"])

        tournament = cls(tournament_serialized["name_tournament"], tournament_serialized["location"],
                         tournament_serialized["start_date"], tournament_serialized["end_date"], tournament_serialized["nb_round"], tournament_serialized["description"])

        return tournament

    def create_round(self):
        """
        Créer un round.
        """
        if len(self.rounds) <= self.nb_round:
            # Nom correspondant au tour.
            round_name = f"Round {len(self.rounds) + 1}"
            round = Round(round_name)
            self.rounds.append(round)
            return round
        else:
            print("Le tournoi est terminé.")
            exit()


class Round:
    """ Création de l'entité Round."""

    def __init__(self, round_name: str):
        self.round_name = round_name
        self.start_datetime = datetime.now()
        # self.end_datetime = self.round_finished()
        self.matches = []

    def __str__(self):
        """Retourne round info en liste"""
        return self.round_name

    def __repr__(self):
        """Retourne round infos"""
        return f'"Nom du tour": {self.round_name} "Début": {self.start_datetime} "Les matches": {self.matches}'

    def round_finished(self):
        """Marque la fin du round.

        Returns:
            _type_: _description_
        """
        return datetime.now()

    def get_match_pairing(self, player_1, player_2):
        """Set match paring as tuple"""
        match = (
            f"{player_1['last_name']}, {player_1['first_name']}",
            player_1["rank"],
            player_1["score"],
            f"{player_2['last_name']}, {player_2['first_name']}",
            player_2["rank"],
            player_2["score"]
        )
        self.matches.append(match)


class Match:
    """
    Le Match.
    """

    def __init__(self, player_1: Player, player_2: Player, score_player_1: float = 0,  score_player_2: float = 0):
        """Création de l'entité Match.

        Args:
            player_1 (Joueur): Le premier joueur.
            player_2 (Joueur): Le second  joueur.
        """
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2

    def __str__(self):
        """
        Méthode pour afficher les détails du match
        """
        return f"Joueur 1: {self.player_1} - point: {self.score_player_1} ::: Joueur 2: {self.player_2} - point: {self.score_player_2}"

    def __repr__(self):
        """
        Méthode pour representer le match
        """

        return ([{self.player_1}, {self.score_player_1}], [{self.player_2}, {self.score_player_2}])


if __name__ == "__main__":
    """
    Tests
    """

    # player1 = Player("William", "Mopete", "AB12345", date(1962, 4, 14))
    # print(player1)
    # print(player1.player_serialize())
    # player1.save_club_player()

    # player_serialized = {
    #     "first_name": "William",
    #     "last_name": "Mopete",
    #     "chess_id": "AB123",
    #     "birthday": "1962-04-14"
    # }

    # player = Player.player_deserialize(player_serialized)
    # print(player)

    # print(Player.display_club_players())

    # player2 = Player("Nelly", "Mopete", "AB98745", date(1964, 6, 2))
    # print(player2)
    # # print(player2.get_player_in_dictionnary_format())
    # player2.save_player()

    tournament_1 = Tournament("Mairie", "l'Hay", datetime(
        2024, 4, 18), datetime(2024, 4, 18), 4, "ras")
    print(tournament_1)
    print(tournament_1.tournament_serialize())
    # tournament_1.save_tournament()
    created_round = tournament_1.create_round()
    print(created_round)
    print(tournament_1.rounds)
