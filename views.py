import dateparser
from datetime import datetime, date
import rich


class View:

    # MENU DEMARRER

    @classmethod
    def display_boot_menu(cls):
        rich.print("-" * 100)
        display_message = """Que souhaitez-vous faire ?
                              1 - Ajouter un(des) joueur(s) au club.
                              2 - Créer et démarrer un tournoi.
                              3 - Générer les rapports.
                              4 - Charger un tournoi.
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
        chess_id = input("Entrer l'identifiant Echecs: ")

        birthday = dateparser.parse(
            input("Entrer la date de naissance du joueur: "))
        if birthday is None:
            birthday = datetime.now()

        return first_name, last_name, chess_id, birthday
    
    @classmethod
    def finish_to_register_players_in_club(cls):
        """Demande la saisie de joueurs à inscrire au club est finie
        """
        finish = input("voulez-vous inscrire un joueur ? (o/n) : ")
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
            input("Entrer la date de début du tournoi(si vous ne saisisez rien la date en cours sera considerez comme date de début ): "))
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

        return (
            name_tournament,
            location, start_date,
            end_date,
            nb_round,
            description
                )

    @classmethod
    def display_tournament(cls, tournament):
        rich.print("-" * 100)
        rich.print(tournament)

    @classmethod
    def ask_number_of_players(cls):
        """Demande le nombre de joueurs à saisir
        """
        number_of_players = int(input(
            "Combien des joueurs voulez-vous ajouter au tournoi ?"))
        if number_of_players is None:
            number_of_players = 1

        return number_of_players
    
    @classmethod
    def go_on_tournament(cls):
        rich.print("-" * 100)
        rich.print("C'est parti pour le tournoi.")

    @classmethod
    def display_round(cls, round):
        rich.print("-" * 100)
        rich.print(round)

    @classmethod
    def go_on_matches(cls, round_name):
        rich.print("-" * 100)
        rich.print(f"Voici les matchs du {round_name}:\n") 

    @classmethod
    def display_round_matches(cls, k, match):
        rich.print(f"Match {k+1}>>>>>>")               
        rich.print(match, "\n\n")

    @classmethod
    def ask_for_report_choice(cls):
        display_message = """Quel rapport souhaitez-vous obtenir ?
                           1 - Afficher la liste de tous les joueurs inscrits 
                                au club.
                           2 - Afficher la liste des tournois dejà orgnanisés.                           
                           3 - Rechercher un tournoi spécifique et Afficher 
                                les informations associées.
                           4 - Afficher la liste des joueurs du tournoi par 
                                ordre alphabétique.
                           5 - Afficher la liste de tous les tours du tournoi 
                                et de tous les matchs du tour.
                           q - Quitter
                           """

        rich.print(display_message)        
        report_choice = input("Votre choix: ")
        return report_choice

    @classmethod
    def display_club_players(cls, players):
        rich.print("-----------------------------------")
        rich.print()
        rich.print("Liste de tous les joueurs inscrits à notre club:", players)
        

    @classmethod
    def set_player_score(cls, player_first_name, player1_last_name):
        """
        Demande le score du jouer.

        Returns:
            : le score du jouer
        """
        while True:
            score_player = float(
                input(
                    f"Entrer le résultat de {player_first_name} {player1_last_name}"
                    f"[valeur comprise entre (0, 0.5, 1)]: "
                    )
                                )
            if score_player in [0, 0.5, 1]:
                return score_player
            else:
                print("veuillez entrer un chiffre valide")

    @classmethod
    def display_score(cls, score):
        rich.print(score)        

    @classmethod
    def display_match(cls, match):
        """Affiche le joueur.

        Args:
            Match: Les composantes d'un match
        """
        rich.print("-----------------------------------")
        rich.print("Match -->", match)

    @classmethod
    def game_over(cls):
        rich.print("Fin du tournoi")

    @classmethod
    def display_list_of_tournament(cls, list_of_tournaments):
        rich.print("-----------------------------------")
        rich.print()
        rich.print("Liste des tournois déjà organisés par le club:", 
                   list_of_tournaments)

    @classmethod
    def search_a_specific_tournament_informations(cls):
        name_tournament = input("Entrer le nom du tournoi: ")

        return name_tournament


if __name__ == "__main__":
    """Tests
    """
    #     view = View()
    #     # view.ask_for_player_infos()
    #     view.get_match_infos()

    # View.ask_for_report_choice()

    # View.display_boot_menu()
    # finish = View.finish_to_register_players_in_club()

