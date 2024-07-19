"""
Bonjour !
1 : Créer un tournoi
2 : Charger un tournoi non terminé
3 : Générer un rapport pour un tournoi
4 : Quitter

-> 1

Quel est le nom du tournoi ?
-> Blabla

...

Combien de joueurs voulez-vous ajouter au tournoi ?
-> 4

# Joueur 1
Nom du joueur ?
-> Mopete

...

# Joueur 2

...

# Joueur 4

C'est parti pour le tournoi.

---- Round 1 -----

-- Match 1 --
William (#dsjqkd) contre Nelly (#dsqhd)

Qui a gagné ?
1 : William
2 : Nelly
3 : Match nul

-> 1

-- Match 2 --
....

---- Round 2 -----

-- Match 1 --
...


Bravo au gagnant William !
Voici le classement final

-----
-
-
-
------

1 : Créer un tournoi
2 : Charger un tournoi
3 : Générer un rapport pour un tournoi
4 : Quitter

-> 3

Choisissez un tournoi :
1 : Tournoi 23/02/2023
2 : ...


-> 1

Quel rapport voulez-vous générer ?
1 : Liste des joueurs
2 : Classement final
3 : Liste des matchs joués

-> 1

"""
from datetime import datetime, date
import dateparser
import random
import rich

from models import Tournament, Player, Round, Match
from views import View


class Controller:
    """Le controleur
    """

    def __init__(self):
        """
        Initialisation du Controleur du tournoi.
        """
     
    # LANCEMENT.
    @classmethod
    def run(cls):
        """Méthode de lancement.
        """
        cls.boot_menu()

    @classmethod
    def boot_menu(cls):

        while True:

            user_choice = View.display_boot_menu()

            # Ajouter de(s) joueur(s) au club
            if user_choice == "1":
                cls.get_club_player()

            # Créer un tournoi
            elif user_choice == "2":
                cls.create_a_tournament()

            # Voir les rapports
            elif user_choice == "3":
                cls.generate_report()
            
            # Charger un tournoi
            elif user_choice == "4":
                cls.load_an_tournament()    

            # Quitter
            elif user_choice == "q":
                cls.quit()

    @classmethod
    def get_club_player(cls):
        """Inscrit un joueur au club.

        Returns:
            incription au club.
        """

        while True:
            player_data = View.ask_for_player_infos()
            player = Player(*player_data)
            View.display_player(player)
            player.save_club_player()

            finish = View.finish_to_register_players_in_club()
            
            if finish != "o":
                break

        return

    @classmethod
    def create_a_tournament(cls):
        """
        Creationd'un tournoi

        Returns:
            Tuple: Contient les informations du tournois.
        """
        tournamant_infos = View.request_tournament_infos()
        tournament = Tournament(*tournamant_infos)
        View.display_tournament(tournament)
        Tournament.tournaments.append(tournament)
        cls.register_tournament_player(tournament)
        View.go_on_tournament()
        players = tournament.players
        nb_round = tournament.nb_round
        rounds = tournament.rounds
        
        for i in range(0, nb_round):                            
            round_name = f"Round {i + 1}"               
            round = Round(round_name)
            View.display_round(round)
            View.go_on_matches(round_name)
            
            if round_name == "Round 1":
                # Au premier tour, mélanger directement les joueurs.
                random.shuffle(players)
                          
            else:
                # Pour les autres tours, trier les joueurs par score_total.
                players = [player.player_serialize() for player in players]                        
                players = sorted(
                    players,
                    key=lambda x: x["score_total"],
                    reverse=True
                                )                    

                players = [
                    Player.player_deserialize(player) for player in players
                            ]
                                        
            cls.pairing_display_scores(round, players)                    

            tournament.rounds.append(round)
        tournament.save_tournament()
        tournament.whos_won()
        return tournament
                        
    @classmethod
    def pairing_display_scores(cls, round, players):
        """
        Crée des paires pour les matchs et saisie les scores.
        """
        matches_increment =[]  
        for j in range(0, len(players), 2):
            player_1 = players[j]
            player_2 = players[j+1]
            match = Match(
                player_1,
                player_2
                            )
            matches_increment.append(match)              
            # round.matches.append(match)

        matches = round.matches
        matches += matches_increment
                 
        for k, match in enumerate(matches_increment):
            View.display_round_matches(k, match)
        
        for match in matches_increment:

            player_1 = match.player_1
            player_2 = match.player_2

            player_1.score = View.set_player_score(
                player_1.first_name, player_1.last_name)
            if player_1.score == 1:
                player_2.score = 0

            elif player_1.score == 0.5:
                player_2.score = 0.5

            elif player_1.score == 0:
                player_2.score = 1

            player_1.score_total += player_1.score
            player_2.score_total += player_2.score

            score = (
                f"{player_1.first_name} {player_1.last_name}\n"
                f" Score sur le match = {player_1.score}"
                f" et "
                f" Score cumulé = {player_1.score_total}\n\n"

                f"{player_2.first_name} {player_2.last_name}\n"
                f" Score sur le match = {player_2.score}"
                f" et "
                f" Score cumulé = {player_2.score_total}\n\n"
                    )

            View.display_score(score)
        round.round_finished()

    @classmethod
    def register_tournament_player(cls, tournament: Tournament):
        """Saisie et Crée un joueur pour le tournoi.

        Returns:
            Joueur: retourne une instance de Joueur du tournoi.
         """

        number_of_players = View.ask_number_of_players()

        for i in range(0, number_of_players):
            player_data = View.ask_for_player_infos()
            player = Player(*player_data)
            View.display_player(player)
            tournament.players.append(player)
            
            # Sauvegarde également le joueur dans le club.
            player.save_club_player()    


    @classmethod
    def generate_report(cls):
        """
        Générer un rapport.
        """
        report_choice = View.ask_for_report_choice()        

        if report_choice == "1":
            # Affiche les joueurs du club.
            players = Player.display_club_players()
            View.display_club_players(players)

        elif report_choice == "2":
            # Affiche la liste de tous les tournois déjà organisés.           
            list_of_tournaments = Tournament.display_list_of_tournament()
            View.display_list_of_tournament(list_of_tournaments)

        elif report_choice == "3":
            # Rechercher un tournoi spécifique et Affiche les informations associées.                 
            name_tournament = View.search_a_specific_tournament_informations()
            Tournament.search_a_specific_tournament_informations(name_tournament)            

        elif report_choice == "3":
            cls.display_tournaments()

        elif report_choice == "4":
            cls.display_players_in_tournament()

        elif report_choice == "q":
            cls.quit()
    
    @classmethod
    def load_an_tournament(cls):
        pass

    @classmethod
    def quit(cls):
        exit()


if __name__ == "__main__":
    """Tests"""

    # Controller.create_a_tournament()
    # Controller.get_club_player()
    # Controller.display_club_players()
    # Controller.create_a_tournament()
    # Controller.get_club_player()
  
    # Controller.create_a_tournament()
    # Controller.register_tournament_player()
    # Controller.generate_report()
    Controller.create_a_tournament()

    
