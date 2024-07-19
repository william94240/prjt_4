from datetime import datetime, date
from pathlib import Path
import json
import random
import rich


class Player:
    """
    Le joueur.
    """

    def __init__(
            self, 
            first_name: str, 
            last_name: str, 
            chess_id: str,
            birthday: date,        
                 ):
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
        self.score = 0.0
        self.score_total = 0.0            

    def __repr__(self) -> str:
        """Représentation interne du joueur
        Returns:
            str: affiche la représentation du joueur.
        """

        return (f"'first_name': {self.first_name}, "
                f"'last_name': {self.last_name}, "
                f"'chess_id': {self.chess_id}, "
                f"'birthday': {self.birthday}, "
                f"'score': {self.score}, "
                f"'score_total': {self.score_total}"
                )                        

    def __str__(self) -> str:
        """Affichage des détails du joueur
        Returns:
            str: affiche les details sur le joueur.
        """
        return (f"Prénom: {self.first_name}\n"
                f"Nom: {self.last_name}\n"
                f"Identifiant echecs: {self.chess_id}\n"
                f"Date de naissance: {self.birthday}\n"   
                )

    def player_serialize(self):
        """
        Sérialise le joueur en vue de la persistance de données.
        Returns:
            json: retourne des données sous une forme json pour la persistance des données.
        """
        player_serialized = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "chess_id": self.chess_id,
            "birthday": self.birthday.strftime("%Y-%m-%d"),
            "score": self.score,
            'score_total': self.score_total
        }
        return player_serialized
   
    def player_deserialize(self, player_serialized):
        """
        Restaure l'objet player dans sa forme originale.
        """

        player_serialized["birthday"] = date.fromisoformat(
            player_serialized["birthday"])

        player = Player(
            player_serialized["first_name"],
            player_serialized["last_name"],
            player_serialized["chess_id"],
            player_serialized["birthday"]               
            )
        
        self.score = player_serialized["score"]
        self.score_total = player_serialized["score_total"]

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
   
    def display_club_players(self):
        """Affiche les joueurs inscrits au club.
        """

        file_path = Path.cwd()/"data"/"club_players.json"

        with open(file_path, "r", encoding="utf-8") as f:
            players_serialized = json.load(f)

            players = [
                self.player_deserialize(player_serialized).__str__(
                ).replace("\n","  ")
                for player_serialized in players_serialized
                      ]
            players = sorted(players, key=lambda x: x.split()[3])         

        return players


class Tournament:

    """Le tournoi.
    """
    # Liste des tournois.
    tournaments = []

    def __init__(
                 self, name_tournament: str,
                 location: str,
                 start_date: datetime,                
                 end_date: datetime,                
                 nb_round: int = 4,
                 description: str = "",           
                 ):
        """Creation Tournoi.

        Args:
            name_tournament (str): Le nom du tournoi
            location (str): Le lieu du tournoi
            start_date (datetime): La date de début du tournoi
            end_date (datetime): La date de fin du tournoi
            nb_round (int, optional): Le nombre de tours du tournoi.
              Defaults to 4.
            description (str, optional): La description du tournoi. 
              Defaults to "".
        """      

        self.name_tournament = name_tournament
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.nb_round = nb_round
        self.description = description
        self.players = []
        self.rounds = []               

    def __repr__(self):
        """Méthode pour une representation interne du tournoi

        Returns:
            str: affiche les details sur le joueur.
        """

        return (
                f'"name_tournament": {self.name_tournament} ',
                f'"location": {self.location}, '
                f'"start_date": {self.start_date}, '
                f'"end_date": {self.end_date}, '
                f'"nb_round": {self.nb_round}, '
                f'"description": {self.description} '
                f'"players": {self.players} '
                f'"rounds": {self.rounds} '               
                )
        
    def __str__(self):
        """
        Méthode pour afficher les détails sur le tournoi
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
        Sérialize le tournoi en de la persistance de données dans un fichier json.

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
            "rounds": self.rounds
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
    
    def tournament_deserialize(self, tournament_serialized):
        """
        Restaure le tournoi en sa forme originales.
        """
        tournament = Tournament(
            tournament_serialized["name_tournament"],
            tournament_serialized["location"],
            date.fromisoformat(tournament_serialized["start_date"]),
            date.fromisoformat(tournament_serialized["end_date"]),
            tournament_serialized["nb_round"],
            tournament_serialized["description"],       
                         )

        self.players = [Player.player_deserialize(self, player) 
                        for player in tournament_serialized["players"]]
        self.rounds = [Round.round_deserialize(self, round)   
                       for round in tournament_serialized["rounds"]]

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

    def display_list_of_tournament(self):
        """Affiche la liste des tournois déjà organisés par le club.
        """

        file_path = Path.cwd()/"data"/"tournaments.json"

        with open(file_path, "r", encoding="utf-8") as f:
            tournaments_serialized = json.load(f)
            # rich.print(tournaments_serialized)      
            tournaments = [self.tournament_deserialize(tournament_serialized)
                           .__str__().replace("\n", "   ") 
                           for tournament_serialized in tournaments_serialized] 
            # rich.print(tournaments)
            list_of_tournaments = sorted(tournaments, 
                                         key=lambda x: x.split()[3])
            # list_of_tournaments = [name_of_tournament.split()[3]
            #                        for name_of_tournament 
            #                        in list_of_tournaments]
            
            rich.print(list_of_tournaments)
        
        return list_of_tournaments
    
    def search_a_specific_tournament_informations(self, name_tournament):
        """Rechercher un tournoi spécifique et afficher les informations 
            associées.
        """
        file_path = Path.cwd()/"data"/"tournaments.json"
        # name_tournament = "ggg"
        with open(file_path, "r", encoding="utf-8") as f:
            tournaments_serialized = json.load(f)
            # print(tournaments_serialized)
            for tournament_serialized in tournaments_serialized:
                # print(tournament_serialized)
                # print(tournament_serialized.keys())
                if tournament_serialized["name_tournament"] == name_tournament:
                    tournament = self.tournament_deserialize(
                        tournament_serialized)                         
                    # rich.print(tournament_serialized)
                    rich.print(tournament)
                    self.players = [Player.player_deserialize(self, player) 
                                    for player in 
                                    tournament_serialized["players"]
                                    ]
                    self.rounds = [Round.round_deserialize(self, round)   
                                   for round in tournament_serialized["rounds"]
                                    ]
                    rich.print(self.players)
                    rich.print(self.rounds)
      
        return tournament
    
    def whos_won(self):
        """Affiche le joueur ayant le plus grand score.
        """
        self.players = sorted(
            self.players, key=lambda x: x.score_total, 
            reverse=True
                              )
        rich.print(self.players)


class Round:
    """ Création de l'entité Round."""

    def __init__(
                 self, 
                 round_name: str,
                 start_datetime: datetime = datetime.now(),
                 end_datetime: datetime = None,
                 ):
        
        self.round_name = round_name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.matches = []

    def __str__(self):
        """Affiche les informations sur le tour"""
        return (
                f"Nom du tour: {self.round_name}\n"
                f"Début: {self.start_datetime}\n"
                f"Fin: {self.end_datetime}\n"                               
                )

    def __repr__(self):
        """Retourne la représentation interne du tour"""
        return (f'"round_name": {self.round_name}, '
                f'"start_datetime": {self.start_datetime}, '
                f'"end_datetime": {self.end_datetime} '
                f'"matches": {self.matches} '
                )

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
            "end_datetime":(
                "Null" if self.end_datetime is None
                else self.end_datetime.strftime("%Y-%m-%d")
                ),
            "matches": self.matches
            }        
        
        round_serialized["matches"] = [
            match.match_serialize()
            for match in self.matches
                                      ]        

        return round_serialized    
    
    def round_deserialize(self, round_serialized):
        """
        Restaure le round dans sa forme originelle.
        """
   
        round = Round(
                      round_serialized["round_name"],
                      date.fromisoformat(round_serialized["start_datetime"]),
                      (None if round_serialized["end_datetime"] is None else
                       date.fromisoformat(round_serialized["end_datetime"]))                     
                     )     

        self.matches = [
            Match.match_deserialize(self, match_serialized)
            for match_serialized in round_serialized["matches"]
              ]

        return round
    

class Match:
    """
    Le Match.
    """

    def __init__(
                 self, 
                 player_1: Player, 
                 player_2: Player
                 ):
        
        """Création de l'entité Match.

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
            f"Joueur: {self.player_1.__str__()}\n\n"            
            f"::::CONTRE::::\n\n"
            f"Joueur: {self.player_2.__str__()}\n"            
                )

    def __repr__(self):
        """
        Méthode pour representer le match en interne.
        """
        return (
            f'"player_1": {self.player_1},'
            f'"player_2": {self.player_2}'
               )
   
    def match_serialize(self):
        """
        Sérialise le match en vue de la persistance de données.

        Returns:
            json: retourne des données sous une forme json pour la persistance.

        """           
        match_serialized = {
            "player_1": self.player_1,           
            "player_2": self.player_2
                            } 

        match_serialized["player_1"] = self.player_1.player_serialize()
        match_serialized["player_2"] = self.player_2.player_serialize()
        
        return match_serialized
   
    def match_deserialize(self, match_serialized):
        """
        Restaure le match dans sa forme originale.
        """

        match = Match(
            match_serialized["player_1"],
            match_serialized["player_2"]
                    )
        
        match_serialized["player_1"] = Player.player_deserialize(
            self, match_serialized["player_1"]
            )
        match_serialized["player_2"] = Player.player_deserialize(
            self, match_serialized["player_2"]
            )    

        return match


if __name__ == "__main__":
    """
    Tests
    """

    # player1 = Player("William", "Mopete", "AB12345", date(1962, 4, 14))
    # player_serialized = player1.player_serialize()    
    # print(player1)
    # print(player1.player_serialize())
    # player_serialized = player1.player_serialize()
    # player = Player.player_deserialize(player_serialized)
    # print(player)
    # player1.save_club_player()
    # print(Player.display_club_players())
    # player2 = Player("Nelly", "Mopete", "AB98745", date(1964, 6, 2))
    # print(player2)

    # print(player1)

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
    # tournament_1.create_round()

    # players = Player.display_club_players()
    # rich.print(players)
    # pprint(players)

    # Tournament.display_list_of_tournament()
    # Tournament.search_a_specific_tournament_informations("kkk")

    # a = Player.display_club_players()
    # rich.print(a)
    # tournament_1.tournament_serialize()
    # tournament_1.display_list_of_tournament()
    # print(player1.display_club_players())
    # tournament_1.search_a_specific_tournament_informations("ggg")
    tournament_1.whos_won()

    