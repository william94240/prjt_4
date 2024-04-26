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


from models import Tournament, Player, Match
from views import View


class Controller:
    """Le controleur
    """

    def __init__(self):
        """
        Initialisation du Controleur du tournoi.
        """

    @classmethod
    def boot_menu(cls):

        while True:

            user_choice = View.display_boot_menu()

            if user_choice == "1":
                cls.create_a_tournament()

            # Charger un tournoi
            elif user_choice == "2":
                cls.load_an_tournament()

            # Ajouter de(s) joueur(s) au club
            elif user_choice == "3":
                cls.get_club_player()

            # Voir les rapports
            elif user_choice == "4":
                cls.generate_report()

            # Quitter
            elif user_choice == "q":
                cls.quit()

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
        cls.register_tournament_player()
        tournament.save_tournament()

        # self.create_round()

    @classmethod
    def register_tournament_player(cls):
        """Saisie et Crée un joueur pour le tournoi.

        Returns:
            Joueur: retourne une instance de Joueur du tournoi.
        """
        # number_of_players = View.ask_number_of_players()

        # for player in range(0, number_of_players):
        player_data = View.ask_for_player_infos()
        player = Player(*player_data)
        View.display_player(player)
        Tournament.add_tournament_player(player)

        return player

    @classmethod
    def get_club_player(cls):
        """Crée un joueur.

        Returns:
            Joueur: retourne une instance joueur.
        """
        # number_of_players = View.ask_number_of_players()

        # for player in range(0, number_of_players):
        player_data = View.ask_for_player_infos()
        player = Player(*player_data)
        View.display_player(player)
        player.save_club_player()

        return

    @classmethod
    def load_an_tournament(cls):
        pass

    @classmethod
    def generate_report(cls):
        """
        Générer un rapport.
        """
        report_choice = View.ask_for_report_choice()

        if report_choice == "1":
            cls.display_club_players()

        elif report_choice == "2":
            cls.display_tournaments()

        elif report_choice == "3":
            cls.display_players_in_tournament()

        elif report_choice == "q":
            cls.quit()

    @classmethod
    def quit(cls):
        exit()

    # LANCEMENT.

    @classmethod
    def run(cls):
        """Méthode de lancement.
        """
        cls.boot_menu()

############### LES METHODES POUR GENERER DES RAPPORTS ###############

    @classmethod
    def display_club_players(cls):
        """Affiche les joueurs du club.
        """
        players = Player.display_club_players()
        View.display_club_players(players)

    @classmethod
    def display_tournaments(cls):
        """Affiche les tournois.
        """
        # tournaments = Tournament.get_tournaments()
        # View.display_tournaments(tournaments)

    @classmethod
    def display_players_in_tournament(cls):
        """Affiche les joueurs inscrits à un tournoi.
        """
        # tournament = Tournament.get_tournament()
        # players = tournament.get_players()
        # View.display_players_in_tournament(players)


############# RESTES ###############

    @classmethod
    def create_round(cls):
        pass

    @classmethod
    def create_match(cls):
        """Créér un match.

        Returns:
            match: _description_
        """
        match_data = View.get_match_infos()
        # match = Match(**match_data)
        View.display_match(match)
        return match


if __name__ == "__main__":
    """Tests"""

    # Controller.create_a_tournament()
    # Controller.get_club_player()
    # Controller.display_club_players()
    Controller.create_a_tournament()
