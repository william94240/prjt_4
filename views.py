import dateparser
from datetime import datetime, date
import rich


class View:

    # MENU DEMARRER

    @classmethod
    def display_boot_menu(cls):
        rich.print("-" * 100)
        display_message = """Que souhaitez-vous faire ?
                              1 - Ajouter de(s) joueur(s) au club.
                              2 - Créer et démarrer un tournoi.
                              3 - Charger un tournoi.
                              4 - Générer les rapports.
                              q - Quitter.
                           """

        rich.print(display_message)
        user_choice = cls.user_input()
        return user_choice

    @classmethod
    def user_input(cls):
        choice = input("Votre choix: ")
        return choice
        
    @classmethod
    def ask_for_player_infos(cls):
        """
            Demande les infos sur le joueur.

            Returns:
                tuple: un tuple d'infos
        """

        rich.print("-" * 100)

        first_name = input("Entrer le prénom du joueur: ")
        last_name = input("Entrer le nom du joueur: ")
        chess_id = input("Entrer l'dentifiant Echecs: ")

        birthday = dateparser.parse(
            input("Entrer la date de naissance du joueur: "))
        if birthday is None:
            birthday = datetime.now()

        return first_name, last_name, chess_id, birthday
    
    @classmethod
    def finish_to_register_players_in_club(cls):
        """Demande la saisie de joueurs à inscrire au club est finie
        """
        finish = input("voulez-vous inscrire un joueur ? (o/n) : " )       
        return finish
    
    
    @classmethod
    def display_player(cls, player):
        """Affiche le joueur.

            Args:
                player (Player): Un joueur
        """
        rich.print("-" * 100)
        rich.print(player)

    @classmethod
    def request_tournament_infos(cls):
        """
        Demande d'infos,sur le tounoi.

        Returns:
            tuple: un tuple d'infos

        """

        rich.print("Bonjour")
        rich.print("-" * 100)

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
        rich.print("-" * 100)
        rich.print(tournament)



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
    def display_round(cls, round):
        rich.print("-" * 100)
        rich.print(round)

    @classmethod
    def go_on_tournament(cls):
        rich.print("-" * 100)
        rich.print("C'est parti pour le tournoi.")

    @classmethod
    def go_on_match(cls):
        rich.print("-" * 100)
        rich.print("Voici les matches du round: ") 

    @classmethod
    def display_round_matches(cls, i, match):
        print(f"Match {i+1}")               
        rich.print(match)  


    @classmethod
    def ask_for_report_choice(cls):
        display_message = """Quel rapport souhaitez-vous obtenir ?
                           1 - Afficher les joueurs inscrits au club 
                           2 - Afficher la liste des tournois dejà orgnanisés
                           3 - Afficher les joueurs inscrits à chaque tournoi
                           q - Quitter
                           """

        rich.print(display_message)
        user_choice = cls.user_input()
        return user_choice

    @classmethod
    def display_club_players(cls, players):
        rich.print("-----------------------------------")
        rich.print()
        rich.print("Liste des joueurs inscrits à notre club:")
        for player in players:
            rich.print(player)

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
        rich.print("-----------------------------------")
        rich.print("Match -->", match)


if __name__ == "__main__":
    """Tests
    """
    #     view = View()
    #     # view.ask_for_player_infos()
    #     view.get_match_infos()

    # View.ask_for_report_choice()

    # View.display_boot_menu()
    # finish = View.finish_to_register_players_in_club()

