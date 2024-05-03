import dateparser
from datetime import datetime, date


class View:

    # MENU DEMARRER

    @classmethod
    def display_boot_menu(cls):
        display_message = ("Que souhaitez-vous faire ?\n"
                           "1 - Créer et démarrer un tournoi\n"
                           "2 - Charger un tournoi\n"
                           "3 - Ajouter de(s) joueur(s) au club\n"
                           "4 - Générer les rapports\n"
                           "q - Quitter\n> "
                           )

        print(display_message)
        user_choice = cls.user_input()
        return user_choice

    @classmethod
    def user_input(cls):
        choice = input("Votre choix: ")
        return choice

    @classmethod
    def request_tournament_infos(cls):
        """
        Demande d'infos,sur le tounoi.

        Returns:
            tuple: un tuple d'infos

        """

        print("Bonjour")
        print("-----------------------------------")

        name_tournament = input("Entrer le Nom du tournoi: ")
        location = input("Entrer le lieu du tournoi: ")

        start_date = dateparser.parse(
            input("Entrer la date de début du tournoi: "))
        if start_date is None:
            # Replace with the appropriate default value
            start_date = datetime.now()

        end_date = dateparser.parse(
            input("Entrer la date de fin du tournoi: "))
        if end_date is None:
            # Replace with the appropriate default value
            end_date = datetime.now()

        nb_round = int(input("Entrer le nombre de tour du tournoi: "))
        description = input("Entrer la description du tournoi: ")

        return (name_tournament, location, start_date, end_date, nb_round, description)

    @classmethod
    def display_tournament(cls, tournament):
        print("Tournoi -->", tournament)

    @classmethod
    def display_round(cls, round):
        print("Tour -->", round)

    @classmethod
    def ask_number_of_players(cls):
        """Demande le nombre de joueurs à saisir
        """
        number_of_players = int(input(
            "Combien de joueurs voulez-vous ajouter au tournoi ?"))
        if number_of_players is None:
            number_of_players = 1

        return number_of_players

    @classmethod
    def ask_for_player_infos(cls):
        """
            Demande les infos sur le joueur.

            Returns:
                tuple: un tuple d'infos
        """

        print("-----------------------------------")

        first_name = input("Entrer le prénom du joueur: ")
        last_name = input("Entrer le nom du joueur: ")
        chess_id = input("Entrer l'dentifiant Echecs: ")

        birthday = dateparser.parse(
            input("Entrer la date de naissance du joueur: "))
        if birthday is None:
            birthday = datetime.now()

        return first_name, last_name, chess_id, birthday

    @classmethod
    def display_player(cls, player):
        """Affiche le joueur.

            Args:
                player (Player): Un joueur
        """
        print("Player:\n", player)

    @classmethod
    def ask_for_report_choice(cls):
        display_message = """Quel rapport souhaitez-vous obtenir ?
                           1 - Afficher les joueurs inscrits au club 
                           2 - Afficher la liste des tournois dejà orgnanisés
                           3 - Afficher les joueurs inscrits à chaque tournoi
                           q - Quitter
                           """

        print(display_message)
        user_choice = cls.user_input()
        return user_choice

    @classmethod
    def display_club_players(cls, players):
        print("-----------------------------------")
        print()
        print("Liste des joueurs inscrits à notre club:")
        for player in players:
            print(player)

    @classmethod
    def get_match_score(cls):
        """
        Demande d'infos à saisir sur le match.

        Returns:
            : un tuple d'infos
        """

        score_player_1 = float(
            input("Entrer le résultat du premier joueur du match [valeur comprise entre (0, 0.5, 1)] : "))
        score_player_2 = float(
            input("Entrer le résultat du second joueur du match [valeur comprise entre (0, 0.5, 1)] : "))

        return [score_player_1, score_player_2]

    @classmethod
    def display_match(cls, match):
        """Affiche le joueur.

        Args:
            Match: Les composantes d'un match
        """
        print("Match -->", match)


if __name__ == "__main__":
    """Tests
    """
    #     view = View()
    #     # view.ask_for_player_infos()
    #     view.get_match_infos()

    View.ask_for_report_choice()
