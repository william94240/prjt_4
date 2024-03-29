from views import View
from models import Tournament


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


from models import Tournament, Player, Match
from views import View


class Controller:
    """Le controleur
    """

    @classmethod
    def boot_menu(cls):
        display_message = ("Que souhaitez-vous faire ?\n"
                           "1 - Créer un tournoi\n"
                           "2 - Charger un tournoi\n"
                           "3 - Créer des joueurs\n"
                           "4 - Voir les rapports\n"
                           "q - Quitter\n> "
                           )

        selections = ["1", "2", "3", "4", "q"]

        message_error = f"Veuiller entrer une valeur valide {
            selections}"

        while True:
            View.display_boot_menu(display_message)
            user_choice = View.user_input()

            if user_choice in selections:
                return user_choice
            else:
                print(message_error)
                continue

            if user_choice == 1:
                pass

            # # Charger un tournoi
            # elif user_choice == "2":
            #     cls.load_an_tournament()

            # # Créer des joueurs
            # elif user_choice == "3":
            #     cls.get_player()

            # # Voir les rapports
            # elif user_choice == "4":
            #     cls.generate_a_report_for_a_tournament()

            # # Quitter
            # else:
            #     cls.quit()

    def __init__(self):
        """
        Initialisation du Controleur du tournoi.
        """
    #     # instatnciation de la vue
    #     self.view = View()

        # Liste pour stocker les tournois

    #     # Liste pour stocker les joueurs du tournois
    #     self.players = []

    tournaments = []

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
        cls.tournaments.append(tournament)
        print(cls.tournaments)
        # self.get_player()
        # self.create_round()

    # LANCEMENT.

    @classmethod
    def run(cls):
        cls.boot_menu()

    def get_player(self):
        """Créer un joueur.

        Returns:
            Joueur: _description_
        """
        player_data = self.view.ask_for_player_infos()
        player = Player(**player_data)
        self.view.display_player(player)
        self.players.append(player)

        return player

    def create_round(self):
        pass

    def create_match(self):
        """Créér un match.

        Returns:
            match: _description_
        """
        match_data = self.view.get_match_infos()
        # match = Match(**match_data)
        self.view.display_match(match)
        return match

    def load_an_tournament(self):
        pass

    def generate_a_report_for_a_tournament(self):
        pass

    @classmethod
    def quit(cls):
        exit()


if __name__ == "__main__":
    pass
#     controler = Controller()
#     controler.create_a_tournament()
#     # controler.get_player()

    Controller.create_a_tournament()
