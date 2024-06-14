from datetime import datetime, date
from pathlib import Path
import json
import random


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

    def __repr__(self) -> str:
        """Représentation interne du joueur

        Returns:
            str: affiche la représentation du joueur.
        """

        return f" 'first_name': {self.first_name}, 'last_name': {self.last_name}, 'chess_id': {self.chess_id}, 'birthday': {self.birthday}"
        

    def __str__(self) -> str:
        """Affichage des détails du joueur

        Returns:
            str: affiche les details sur le joueur.
        """

        return f" Prénom: {self.first_name}\n Nom: {self.last_name}\n Identifiant echecs: {self.chess_id}\n Date de naissance: {self.birthday}"

    def player_serialize(self):
        """
        Sérialise le joueur en de la persistance de données.

        Returns:
            json: retourne des données sous une forme json pour la persistance.ras

        """

        player_serialized = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "chess_id": self.chess_id,
            "birthday": self.birthday.strftime("%Y-%m-%d")
        }

        return player_serialized

    @classmethod
    def player_deserialize(cls, player_serialized):
        """
        Restaure le player dans sa forme originale.
        """

        player_serialized["birthday"] = date.fromisoformat(
            player_serialized["birthday"])

        player = cls(player_serialized["first_name"], player_serialized["last_name"],
                     player_serialized["chess_id"], player_serialized["birthday"])

        return player

    def save_club_player(self):
        """Sauvegarde le joueur dans un fichier json.

        Returns:
            _type_: None
        """

        folder_path = Path.cwd()/"data"
        file_path = folder_path/"club_players.json"

        if not file_path.exists():
            folder_path.mkdir(parents=True, exist_ok=True)
            file_path.touch()
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump([], f)

        with open(file_path, "r", encoding="utf-8") as f:
            players = json.load(f)

        player_serialized = self.player_serialize()
        players.append(player_serialized)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(players, f, indent=4)

    @classmethod
    def display_club_players(cls):
        """Affiche les joueurs inscrits au club.
        """

        file_path = Path.cwd()/"data"/"club_players.json"

        with open(file_path, "r", encoding="utf-8") as f:
            players_serialized = json.load(f)

            players = [cls.player_deserialize(
                player_serialized).__str__().replace("\n", " ") for player_serialized in players_serialized]

        return players


class Tournament:

    """Le tournoi.
    """
    # Liste des tournois.
    tournaments = []

    def __init__(self, name_tournament: str, location: str, start_date: datetime, end_date: datetime,
                 nb_round: int = 4, description: str = ""):
        """Creation Tournoi.

        Args:
            name_tournament (str): Le nom du tournoi
            location (str): Le lieu du tournoi
            start_date (datetime): La date de début du tournoi
            end_date (datetime): La date de fin du tournoi
            nb_round (int, optional): Le nombre de tours du tournoi. Defaults to 4.
            description (str, optional): La description du tournoi. Defaults to "".
        """

        # NB: DOTO ajouter nombre players.

        self.name_tournament = name_tournament
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.nb_round = nb_round
        self.description = description
        self.rounds = []
        self.players = []

    def __repr__(self):
        """Méthode pour une representation interne du tournoi

        Returns:
            str: affiche les details sur le joueur.
        """

        return f'{"name_tournament": {self.name_tournament}, "location": {self.location}, "start_date": {self.start_date}, "end_date": {self.end_date}, "nb_round": {self.nb_round}, "description": {self.description}}'

    def __str__(self):
        """
        Méthode pour afficher les détails sur tournoi
        """

        return f" Nom du tournoi: {self.name_tournament}\n Lieu: {self.location}\n Date début: {self.start_date}\n Date fin: {self.end_date}\n Nombre de Tours: {self.nb_round}\n Description: {self.description}\n Les joueurs: {self.players}\n Les rounds: {self.rounds}\n"


    def tournament_serialize(self):
        """
        Sérialize le tournoi en de la persistance de données.

        Returns:
            données serialisées: données sous forme json pour la persistance.
        """

        tournament_serialized = {
            "name_tournament": self.name_tournament,
            "location": self.location,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "nb_round": self.nb_round,
            "description": self.description,
            "players": self.players,
            "number_rounds": self.nb_round,
            "rounds": self.rounds

        }

        tournament_serialized["players"] = [
            player.player_serialize() for player in self.players]
        
        tournament_serialized["rounds"] = [
            round.round_serialize() for round in self.rounds]

        return tournament_serialized

    @classmethod
    def tournament_deserialize(cls, tournament_serialized):
        """
        Restaure le tournoi en sa forme originales.
        """

        tournament_serialized["start_date"] = date.fromisoformat(
            tournament_serialized["start_date"])
        tournament_serialized["end_date"] = date.fromisoformat(
            tournament_serialized["end_date"])

        tournament = cls(tournament_serialized["name_tournament"], tournament_serialized["location"],
                         tournament_serialized["start_date"], tournament_serialized["end_date"], tournament_serialized["nb_round"], tournament_serialized["description"])

        return tournament

    def save_tournament(self):
        """Sauvegarde le tounoi dans un fichier tournaments.json.

        Returns:
            _type_: _description_

        """

        folder_path = Path.cwd()/"data"
        file_path = folder_path/"tournaments.json"

        if not file_path.exists():
            folder_path.mkdir(exist_ok=True, parents=True)
            file_path.touch()
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump([], f)

        with open(file_path, "r", encoding="utf-8") as f:
            tournaments = json.load(f)
            tournament_serialized = self.tournament_serialize()
            tournaments.append(tournament_serialized)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(tournaments, f, indent=4)

    def create_round(self):
        """
        Créer un round.
        """
        if len(self.rounds) <= self.nb_round:
            # Création du nom correspondant au tour.
            round_name = f"Round {len(self.rounds) + 1}"
            round = Round(round_name)

            if round_name == "Round 1":
                random.shuffle(self.players)

            # TODO :Sinon Trier les joueurs par rang(rank).
            for i in range(0, len(self.players), 2):
                match = Match(self.players[i], self.players[i+1])                
                round.matches.append(match)
            self.rounds.append(round)

            # print(self.players)
            # print(self.rounds)
            # print(round.matches)


            return round
        else:
            print("Le tournoi est terminé.")
            exit()


class Round:
    """ Création de l'entité Round."""

    def __init__(self, round_name: str):
        self.round_name = round_name
        self.start_datetime = datetime.now()
        self.end_datetime = None
        self.matches = []

    def __str__(self):
        """Retourne les informations sur le Tour"""
        return f" Nom du tour: {self.round_name}\n Début: {self.start_datetime}\n Fin: {self.end_datetime}"

    def __repr__(self):
        """Retourne la représentation interne du Tour"""
        return f'"round_name": {self.round_name}, "start_datetime": {self.start_datetime}, "end_datetime": {self.end_datetime}'

    def round_finished(self):
        """Marque la fin du round.

        Returns:
            _type_: _description_
        """
        self.end_datetime = datetime.now()
        return self.end_datetime
    


    def round_serialize(self):
        """
        Sérialise le round en vue de la persistance de données.

        Returns:
            json: retourne des données sous une forme json pour la persistance.

        """
        
        round_serialized = {
            "round_name": self.round_name,
            "start_datetime": self.start_datetime.strftime("%Y-%m-%d"),
            "end_datetime": None if self.end_datetime is None else self.end_datetime.strftime("%Y-%m-%d"),
            "matches": self.matches
            
        }

        round_serialized["matches"] = [
            match.match_serialize() for match in self.matches]


        return round_serialized

    @classmethod
    def round_deserialize(cls, round_serialized):
        """
        Restaure le round dans sa forme originale.
        """

        round_serialized["start_datetime"] = date.fromisoformat(
            round_serialized["start_datetime"])
        
        round_serialized["end_datetime"] = date.fromisoformat(
            round_serialized["end_datetime"])

        round = cls(round_serialized["round_name"], round_serialized["start_datetime"],
                     round_serialized["end_datetime"], round_serialized["matches"])

        return round



    # def get_match_pairing(self, player_1, player_2):
    #     """Set match pairing as tuple"""
    #     match = (
    #         f"{player_1['last_name']}, {player_1['first_name']}",
    #         player_1["rank"],
    #         player_1["score"],
    #         f"{player_2['last_name']}, {player_2['first_name']}",
    #         player_2["rank"],
    #         player_2["score"]
    #     )
    #     self.matches.append(match)


class Match:
    """
    Le Match.
    """

    def __init__(self, player_1: Player, player_2: Player):
        """Création de l'entité Match.

        Args:
            player_1 (Joueur): Le premier joueur entré.
            player_2 (Joueur): Le second  joueur entré.
        """
        self.player_1 = player_1
        self.player_2 = player_2
        # self.score_player_1 = score_player_1
        # self.score_player_2 = score_player_2
        # self.rank_player_1 = self.rank_player_1 + self.score_player_1
        # self.rank_player_2 = self.rank_player_2 + self.score_player_2

    def __str__(self):
        """
        Méthode pour afficher les détails du match
        """
        # return f"Joueur : {self.player_1} - score: {self.score_player_1} rang: {self.rank_player_1}  :::: Joueur : {self.player_2} - point: {self.score_player_2} rang: {self.rank_player_2}"
        return f"Joueur : {self.player_1}\n ::::\n Joueur : {self.player_2}"

    def __repr__(self):
        """
        Méthode pour representer le match
        """

        # return ([{self.player_1}, {self.score_player_1}], [{self.player_2}, {self.score_player_2}])
        return f'{self.player_1.first_name} {self.player_1.last_name} VS  {self.player_2.first_name} {self.player_2.last_name}'
        
    

        


    def match_serialize(self):
        """
        Sérialise le match en vue de la persistance de données.

        Returns:
            json: retourne des données sous une forme json pour la persistance.

        """
        
        match_serialized = {
            "player_1": self.player_1.player_serialize(),
            "player_2": self.player_2.player_serialize(),
                       
        }

        return match_serialized

    @classmethod
    def match__deserialize(cls, match__serialized):
        """
        Restaure le match dans sa forme originale.
        """



        match = cls(match__serialized["player_1"], match__serialized["player_2"])

        return match


if __name__ == "__main__":
    """
    Tests
    """

    player1 = Player("William", "Mopete", "AB12345", date(1962, 4, 14))
    print(player1)
    # print(player1.player_serialize())
    # player_serialized = player1.player_serialize()
    # player = Player.player_deserialize(player_serialized)
    # print(player)
    # player1.save_club_player()
    # print(Player.display_club_players())
    # player2 = Player("Nelly", "Mopete", "AB98745", date(1964, 6, 2))
    # print(player2)

    tournament_1 = Tournament("Mairie", "l'Hay", datetime(
        2024, 4, 18), datetime(2024, 4, 18), 4, "ras")
    # print(tournament_1)
    # tournament1_serialized = tournament_1.tournament_serialize()
    # print(tournament1_serialized)
    # tournament1_deserialized = Tournament.tournament_deserialize(
    #     tournament1_serialized)
    # print(tournament1_deserialized)
    # tournement_player1 = tournament_1.add_tournament_player(player1)
    # tournament_1.save_tournament()

    # created_round = tournament_1.create_round()
    # print(created_round)
    # print(tournament_1.rounds)

    # print(player1.__repr__())
    tournament_1.create_round()

