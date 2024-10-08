from datetime import datetime, date
from pathlib import Path
import json


class Player:
    """
    Le joueur : Définit l'état du joueur et ses comportements à travers
    les méthodes.
    """

    def __init__(
            self,
            first_name: str,
            last_name: str,
            chess_id: str,
            birthday: date,
            ):
        """
        Initialisation de l'instance joueur.
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
        self.score = 0.0
        self.score_total = 0.0

    def __repr__(self) -> str:
        """Représentation interne du joueur
        Returns:
            str: affiche la représentation en mémoire du joueur.
        """

        return (f"'first_name': {self.first_name}, "
                f"'last_name': {self.last_name}, "
                f"'chess_id': {self.chess_id}, "
                f"'birthday': {self.birthday}, "
                f"'score': {self.score}, "
                f"'score_total': {self.score_total}"
                )

    def __str__(self) -> str:
        """Affichage des détails sur le joueur
        Returns:
            str: affiche les details sur le joueur.
        """
        return (f"Prénom: {self.first_name}\n"
                f"Nom: {self.last_name}\n"
                f"Identifiant échecs: {self.chess_id}\n"
                f"Date de naissance: {self.birthday}\n"
                f"Score: {self.score}\n"
                f"Score_total: {self.score_total}\n"
                )

    def player_serialize(self):
        """
        Sérialise le joueur en vue de la persistance de données dans
        un fichier .json.
        Returns:
            json: retourne des données sous une forme d'objet javascript "json"
            pour la persistance des données.
        """
        player_serialized = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "chess_id": self.chess_id,
            "birthday": ((self.birthday.strftime("%Y-%m-%d")) if self.birthday
                         is not None else "null"
                         ),
            "score": self.score,
            'score_total': self.score_total
        }

        return player_serialized

    @classmethod
    def player_deserialize(cls, player_serialized):
        """
        Restaure l'instance player dans sa forme originale.
        """
        player_serialized["birthday"] = date.fromisoformat(
            player_serialized["birthday"]) if player_serialized[
                "birthday"] != "null" else None
        player = cls(
            player_serialized["first_name"],
            player_serialized["last_name"],
            player_serialized["chess_id"],
            player_serialized["birthday"]
            )
        player.score = player_serialized["score"]
        player.score_total = player_serialized["score_total"]

        return player

    def save_club_player(self):
        """Sauvegarde le joueur dans un fichier json.
        """
        file_path = Path.cwd()/"data"/"club_players.json"

        with open(file_path, mode="r", encoding="utf-8") as f:
            players = json.load(f)

        player_serialized = self.player_serialize()
        players.append(player_serialized)

        with open(file_path, mode="w", encoding="utf-8") as f:
            json.dump(players, f, indent=4)

    @classmethod
    def display_club_players(cls):
        """
        Affiche les joueurs inscrits au club.
        """

        file_path = Path.cwd()/"data"/"club_players.json"

        with open(file_path, mode="r", encoding="utf-8") as f:
            players_serialized = json.load(f)

            players = (
                cls.player_deserialize(player_serialized)
                for player_serialized in players_serialized
                      )
            players = sorted(players, key=lambda x: x.last_name)

        return players

    @classmethod
    def chess_id_exist(cls, chess_id):
        """
        Affiche les joueurs inscrits au club.
        """
        file_path = Path.cwd()/"data"/"club_players.json"

        with open(file_path, mode="r", encoding="utf-8") as f:
            players_serialized = json.load(f)

            players = (
                cls.player_deserialize(player_serialized)
                for player_serialized in players_serialized
                      )

        for player in players:
            if player.chess_id == chess_id:
                return player

    @classmethod
    def delete_player(cls, chess_id):
        """
        Supprime un joueur du club.
        """
        file_path = Path.cwd()/"data"/"club_players.json"

        with open(file_path, mode="r", encoding="utf-8") as f:
            players_serialized = json.load(f)

            players = [
                cls.player_deserialize(player_serialized)
                for player_serialized in players_serialized
                      ]

        for player in players:
            if player.chess_id == chess_id:
                players.remove(player)

        players_serialized = [
            player.player_serialize()
            for player in players
            ]

        with open(file_path, mode="w", encoding="utf-8") as f:
            json.dump(players_serialized, f, indent=4)


class Tournament:

    """
    Le tournoi: Fournis les caractéristiques de chaque instance du tournoi.
    """

    tournaments = []

    def __init__(
                 self,
                 name_tournament: str,
                 location: str,
                 start_date: datetime = datetime.now(),
                 end_date: datetime = datetime.now(),
                 nb_round: int = 4,
                 description: str = ""
                ):
        """
        Initialisation de l'instance tournoi.

        Args:
            name_tournament (str): Le nom du tournoi
            location (str): Le lieu du tournoi
            start_date (datetime): La date de début du tournoi
            end_date (datetime): La date de fin du tournoi
            nb_round (int, optional): Le nombre de tours du tournoi.
              par défaut à 4.
            description (str, optionel): La description du tournoi."""

        self.name_tournament = name_tournament
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.nb_round = nb_round
        self.description = description
        self.players = []
        self.rounds = []
        self.nb_player = 0
        self.nb_round_in_progress = 0
        self.nb_player_in_progress = 0

    def __repr__(self):
        """Méthode pour une représentation interne du tournoi

        Returns:
            str: reprensente les details sur le joueur.
        """

        return (
                f'"name_tournament": {self.name_tournament}, '
                f'"location": {self.location}, '
                f'"start_date": {self.start_date}, '
                f'"end_date": {self.end_date}, '
                f'"nb_round": {self.nb_round}, '
                f'"description": {self.description} '
                f'"nb_player": {self.nb_player}, '
                f'"nb_round_in_progress": {self.nb_round_in_progress}, '
                f'"nb_player_in_progress": {self.nb_player_in_progress}, '
                f'"rounds": {self.rounds}, '
                f'"players": {self.players} '
                )

    def __str__(self):
        """
        Méthode qui permet d'afficher les détails sur le tournoi
        """

        return (f"Nom du tournoi: {self.name_tournament}\n"
                f"Lieu: {self.location}\n"
                f"Date début: {self.start_date}\n"
                f"Date fin: {self.end_date}\n"
                f"Nombre de Tours: {self.nb_round}\n"
                f"Description: {self.description}\n"
                )

    def tournament_serialize(self):
        """
        Sérialize le tournoi pour de la persistance de données dans un fichier
        json.

        Returns:
            données serialisées: données sous forme objet javascript pour la
            conservation des données.
        """
        tournament_serialized = {
            "name_tournament": self.name_tournament,
            "location": self.location,
            "start_date": (self.start_date.strftime("%Y-%m-%d %H:%M:%S") if
                           self.start_date is not None else "null"
                           ),
            "end_date": (self.end_date.strftime("%Y-%m-%d %H:%M:%S") if self.end_date
                         is not None else "null"
                         ),
            "nb_round": self.nb_round,
            "description": self.description,
            "nb_player": self.nb_player,
            "nb_round_in_progress": self.nb_round_in_progress,
            "nb_player_in_progress": self.nb_player_in_progress,
            "rounds": self.rounds,
            "players": self.players
                                }

        tournament_serialized["players"] = [
                                            player.player_serialize()
                                            for player in self.players
                                            ]
        tournament_serialized["rounds"] = [
                                           round.round_serialize()
                                           for round in self.rounds
                                           ]

        return tournament_serialized

    @classmethod
    def tournament_deserialize(cls, tournament_serialized):
        """
        Restaure le tournoi sous sa forme objet.
        """
        start_date = datetime.fromisoformat(tournament_serialized["start_date"])
        end_date = datetime.fromisoformat(tournament_serialized["end_date"])

        tournament = cls(
            tournament_serialized["name_tournament"],
            tournament_serialized["location"],
            start_date,
            end_date,
            tournament_serialized["nb_round"],
            tournament_serialized["description"]
            )

        tournament.nb_player = tournament_serialized["nb_player"]
        tournament.nb_round_in_progress = tournament_serialized["nb_round_in_progress"]
        tournament.nb_player_in_progress = tournament_serialized["nb_player_in_progress"]

        tournament.players = [Player.player_deserialize(player)
                              for player in tournament_serialized["players"]
                              ]
        tournament.rounds = [Round.round_deserialize(round)
                             for round in tournament_serialized["rounds"]
                             ]
        return tournament

    def save_tournament(self):
        """Sauvegarde le tounoi dans un fichier tournaments.json.

        Returns:
            None: None
            .pop("name_tournament", None)
        """
        file_path = Path.cwd()/"data"/"tournaments.json"

        with open(file_path, mode="r", encoding="utf-8") as f:
            tournaments_serialized = json.load(f)

            for tournament_serialized in tournaments_serialized:
                if tournament_serialized["name_tournament"] == self.name_tournament:
                    tournaments_serialized.remove(tournament_serialized)

            tournament_serialized = self.tournament_serialize()
            tournaments_serialized.append(tournament_serialized)

        with open(file_path, mode="w", encoding="utf-8") as f:
            json.dump(tournaments_serialized, f, indent=4)

    def whos_won(self):
        """Affiche le joueur ayant le plus grand score.
        """
        players = sorted(
            self.players, key=lambda x: x.score_total,
            reverse=True
                              )
        return players

    def tournament_finished(self):
        """Marque la fin du tournoi.

        Returns:
            _datetime.datetime_: La date de fin du tournoi.
        """
        self.end_date = datetime.now()
        return self.end_date

    @classmethod
    def display_list_of_tournament(cls):
        """Affiche la liste de tournois déjà organisés par le club.
        """

        file_path = Path.cwd()/"data"/"tournaments.json"

        with open(file_path, mode="r", encoding="utf-8") as f:
            tournaments_serialized = json.load(f)

            tournaments = (cls.tournament_deserialize(tournament_serialized)
                           for tournament_serialized in
                           tournaments_serialized
                           )

            list_of_tournaments = sorted(tournaments,
                                         key=lambda x: x.name_tournament
                                         )

        return list_of_tournaments

    @classmethod
    def search_a_specific_tournament_informations(cls, name_tournament):
        """Rechercher un tournoi spécifique et afficher les informations
            associées.
        """
        file_path = Path.cwd()/"data"/"tournaments.json"

        with open(file_path, mode="r", encoding="utf-8") as f:
            tournaments_serialized = json.load(f)

            for tournament_serialized in tournaments_serialized:
                # Cherche si le tuple(name_tournament, name_tournament) est
                # dans tournament_serialized
                if ("name_tournament", name_tournament) in tournament_serialized.items():
                    tournament = cls.tournament_deserialize(tournament_serialized)

                    # Affichage des joueurs du tournoi.
                    players = (player for player in tournament.players)

                    # Affichage des rounds du tournoi.
                    rounds = (round for round in tournament.rounds)

                    # Affichage des matches du tournoi.
                    round_matches = (
                        (round.round_name, round.matches) for round in
                        tournament.rounds
                        )

        return tournament, players, rounds, round_matches

    @classmethod
    def tournament_name_exist(cls, name_tournament):
        """
        Vérifie si le nom du tournoi existe déjà.
        """
        file_path = Path.cwd()/"data"/"tournaments.json"

        with open(file_path, mode="r", encoding="utf-8") as f:
            tournaments_serialized = json.load(f)

            tournaments = [cls.tournament_deserialize(tournament_serialized)
                           for tournament_serialized in tournaments_serialized
                           ]

            for tournament in tournaments:
                if tournament.name_tournament == name_tournament:
                    return f"Le tournoi:\n\n{tournament}\nexiste déjà."

    @classmethod
    def extract_tournament(cls):
        """
        Extrait le dernier tournoi non finis.
        """
        file_path = Path.cwd()/"data"/"tournaments.json"

        with open(file_path, mode="r", encoding="utf-8") as f:
            tournaments_serialized = json.load(f)

            tournaments = [cls.tournament_deserialize(tournament_serialized)
                           for tournament_serialized in tournaments_serialized
                           ]
        return tournaments[-1]


class Round:
    """
    Round produit des instances avec des attributs ci-dessous.
    """

    def __init__(
                 self,
                 round_name: str,
                 start_datetime: datetime = datetime.now(),
                 end_datetime: datetime = datetime.now()
                 ):
        """
        Initialisation de l'instance Round.
        """

        self.round_name = round_name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.matches = []

    def __str__(self):
        """Affiche les informations sur le tour"""
        return (
                f"Nom du tour: {self.round_name}\n"
                f"Début du tour: {self.start_datetime}\n"
                f"Fin du tour: {self.end_datetime}\n"
                )

    def __repr__(self):
        """Retourne la représentation interne du tour"""
        return (f'"round_name": {self.round_name}, '
                f'"start_datetime": {self.start_datetime}, '
                f'"end_datetime": {self.end_datetime} '
                f'"matches": {self.matches} '
                )

    def round_serialize(self):
        """
        Sérialisation du round en vue de la persistance de données.

        Returns:
            json: retourne des données sous une forme json pour la persistance.

        """

        round_serialized = {
            "round_name": self.round_name,
            "start_datetime": (self.start_datetime.strftime("%Y-%m-%d %H:%M:%S") if
                               self.start_datetime is not None else "null"
                               ),
            "end_datetime": (self.end_datetime.strftime("%Y-%m-%d %H:%M:%S") if
                             self.end_datetime is not None else "Null"
                             ),
            "matches": self.matches
            }

        round_serialized["matches"] = [
            match.match_serialize()
            for match in self.matches
                                      ]
        return round_serialized

    @classmethod
    def round_deserialize(cls, round_serialized):
        """
        Restaure le round dans sa forme originelle.
        """

        start_datetime = datetime.fromisoformat(round_serialized["start_datetime"])
        end_datetime = datetime.fromisoformat(round_serialized["end_datetime"])
        round = Round(
                      round_serialized["round_name"],
                      start_datetime,
                      end_datetime
                      )

        round.matches = (
            Match.match_deserialize(match_serialized)
            for match_serialized in round_serialized["matches"]
              )

        return round

    def round_finished(self):
        """Marque la fin du round.

        Returns:
            datetime.datetime: retourne la date de fin du round.
        """
        self.end_datetime = datetime.now()
        return self.end_datetime


class Match:
    """
    Le Match: Décrit les instances à produire du match.
    """

    def __init__(
                 self,
                 player_1: Player,
                 player_2: Player
                 ):

        """Initialisation de l'objet match.

        Args:
            player_1 (Joueur): Le premier joueur entré.
            player_2 (Joueur): Le second  joueur entré.
        """
        self.player_1 = player_1
        self.player_2 = player_2

    def __str__(self):
        """
        Méthode pour afficher les détails du match
        """

        return (
            f"Joueur 1:\n{self.player_1}\n"
            f"::::CONTRE::::\n\n"
            f"Joueur 2:\n{self.player_2}\n"
            )

    def __repr__(self):
        """
        Méthode pour representer le match en interne.
        """
        return (
            f'"player_1": {self.player_1}, "player_2": {self.player_2}'
               )

    def match_serialize(self):
        """
        Sérialise le match en vue de la persistance de données.

        Returns:
            json: retourne des données sous une forme json pour la persistance.

        """
        match_serialized = {
            "player_1": self.player_1.player_serialize(),
            "player_2": self.player_2.player_serialize()
                            }

        return match_serialized

    @classmethod
    def match_deserialize(cls, match_serialized):
        """
        Restaure le match dans sa forme originale.
        """
        player_1 = Player.player_deserialize(match_serialized["player_1"])
        player_2 = Player.player_deserialize(match_serialized["player_2"])

        match = cls(player_1, player_2)

        return match
