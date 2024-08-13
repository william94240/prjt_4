import dateparser
from datetime import datetime
import rich


class View:
    """
    Classe des vues.
    """

    # MENU DEMARRER
    @classmethod
    def display_boot_menu(cls):
        """Affiche le menu de démarrage."""

        rich.print("-" * 100)
        display_message = """Que souhaitez-vous faire ?
                              1 - Ajouter un(des) joueur(s) au club.
                              2 - Créer et démarrer un tournoi.
                              3 - Générer les rapports.
                              q - Quitter.
                           """

        rich.print(display_message)
        user_choice = cls.user_input()
        return user_choice

    @staticmethod
    def user_input():
        """Demande le choix de l'utilisateur."""
        choice = input("Votre choix: ")
        return choice

    @staticmethod
    def ask_for_player_infos():
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

        return (first_name,
                last_name,
                chess_id,
                birthday
                )

    @staticmethod
    def display_player(player):
        """Affiche le joueur.
        """
        rich.print("-" * 100)
        rich.print(player)

    @staticmethod
    def finish_to_register_players_in_club():
        """Demande la saisie de joueurs à inscrire au club est finie
        """
        finish = input("voulez-vous inscrire un joueur ? (o/n) : ")
        return finish

    @staticmethod
    def request_tournament_infos():
        """
        Demande d'infos,sur le tounoi.

        Returns:
            tuple: un tuple d'infos

        """

        rich.print("-" * 100)

        name_tournament = input("Entrer le nom du tournoi: ")
        location = input("Entrer le lieu du tournoi: ")

        start_date = dateparser.parse(
            input(
                """
                Entrer la date de début du tournoi
                (si vous ne saisisez rien, la date en cours sera
                considerez comme date de début du tournoi). ):
                """
                )
                                    )

        if start_date is None:
            # Remplacer par la date en cours par défaut.
            start_date = datetime.now()

        end_date = dateparser.parse(
            input("Entrer la date de fin du tournoi: ")
                                    )
        if end_date is None:
            # Remplacer par la date en cours par défaut.
            end_date = datetime.now()

        nb_round = int(input("Entrer le nombre de tour du tournoi: "))
        description = input("Entrer la description du tournoi: ")

        return (
            name_tournament,
            location,
            start_date,
            end_date,
            nb_round,
            description
                )

    @staticmethod
    def display_tournament(tournament):
        """Affiche le tournoi."""
        rich.print("-" * 100)
        rich.print(tournament)

    @staticmethod
    def ask_number_of_players():
        """Demande le nombre de joueurs à saisir
        """
        number_of_players = int(input(
            "Combien des joueurs voulez-vous ajouter au tournoi ?: "
                                    )
                                )
        if number_of_players is None:
            number_of_players = 1

        return number_of_players

    @staticmethod
    def go_on_tournament():
        """Affiche le début du tournoi."""
        rich.print("-" * 100)
        rich.print("C'est parti pour le tournoi ! \n\n")

    @staticmethod
    def display_round(round):
        """Affiche le tour du tournoi."""
        rich.print("-" * 100)
        rich.print(round)

    @staticmethod
    def go_on_matches(round_name):
        """Affiche l'étiquette du round."""
        # rich.print("-" * 100)
        rich.print(f"Voici les matches du {round_name}:\n")

    @staticmethod
    def display_round_matches(matches_round):
        """Affiche les matchs du round."""
        # rich.print(f"Match {k+1}>>>>>>")
        for k, match_round in enumerate(matches_round):
            rich.print(f"Match {k+1}>>>>>>")
            rich.print(match_round)
        # rich.print(matches, "\n\n")

    @staticmethod
    def want_enter_the_scores_of_the_matches():
        """Demande si vous voulez saisir les scores des matchs."""
        rich.print("-" * 100)
        response = input("Voulez-vous saisir les scores des matchs ?(o/n): ")
        rich.print("")
        return response

    @staticmethod
    def set_player_score(player_first_name, player_last_name):
        """
        Demande le score du jouer.

        Returns:
            : le score du jouer
        """
        while True:
            score_player = float(
                input(
                    f"Entrer le résultat de {player_first_name} "
                    f"{player_last_name} "
                    f"[valeur doit être comprise entre (0, 0.5, 1)]: "
                    )
                                )
            if score_player in [0, 0.5, 1]:
                return score_player
            else:
                print("veuillez entrer un chiffre valide")

    @staticmethod
    def display_score(round_name, k,  score):
        """Affiche le score du match."""
        rich.print(f"<<<<<{round_name}  Match {k+1}>>>>>\n")
        rich.print(score)

    @staticmethod
    def display_match(match):
        """Affiche le joueur.

        Args:
            Match: Les composantes d'un match
        """
        rich.print("-" * 100)
        rich.print("Match -->", match)

    @staticmethod
    def display_winner(winner):
        """Affiche le gagnant du tournoi."""
        rich.print("-" * 100)
        rich.print("La liste des resultats du tournoi suivant l'ordre "
                   "décroissant des scores est:\n"
                   )
        for player in winner:
            rich.print(player)

        rich.print(f"***** Le Vainqeur du tournoi est: *****\n{winner[0]}")

    @staticmethod
    def game_over():
        """Affiche la fin du tournoi."""
        rich.print("Fin du tournoi")

    @staticmethod
    def ask_for_report_choice():
        """Demande le choix du rapport à afficher."""
        display_message = """Quel rapport souhaitez-vous obtenir ?
                           1 - Afficher la liste de tous les joueurs inscrits
                               au club.
                           2 - Afficher la liste des tournois dejà orgnanisés.
                           3 - Rechercher un tournoi spécifique et Afficher
                               les informations associées.
                           q - Quitter
                           """

        rich.print(display_message)
        report_choice = input("Votre choix: ")
        return report_choice

    @staticmethod
    def display_club_players(players):
        """Affiche les joueurs du club."""
        rich.print("-" * 100)
        rich.print()
        rich.print("Liste de tous les joueurs inscrits à notre club: ")
        for player in players:
            rich.print(player)

    @staticmethod
    def display_list_of_tournament(list_of_tournaments):
        """Affiche la liste des tournois déjà organisés par le club."""
        rich.print("-" * 100)
        rich.print("Liste des tournois déjà organisés par le club: \n")
        for tournament in list_of_tournaments:
            rich.print(tournament)

    @staticmethod
    def search_a_specific_tournament_name():
        """Demande le nom du tournoi à rechercher."""
        name_tournament = input("Entrer le nom du tournoi: ")

        return name_tournament

    @staticmethod
    def display_tournament_informations(
            tournament, players, rounds, round_matches
                                        ):
        """Affiche les informations du tournoi."""
        rich.print("-" * 100)
        rich.print("Le tournoi: --->\n")
        rich.print(tournament)
        rich.print("-" * 100)
        rich.print("Les joueurs: --->:\n")
        for player in players:
            rich.print(player)
        rich.print("-" * 100)
        rich.print("Les rounds: --->\n")
        for round in rounds:
            rich.print(round)
        rich.print("-" * 100)
        rich.print("Les matchs: --->\n")
        for round_match in round_matches:
            rich.print(round_match[0])
            for i, match in enumerate(round_match[1]):
                rich.print(f"Match {i+1}>>>>>>")
                rich.print(match.player_1)
                rich.print("--CONTRE--\n")
                rich.print(match.player_2)



            # rich.print(match[1])


if __name__ == "__main__":
    """Tests
    """
    #     view = View()
    #     # view.ask_for_player_infos()
    #     view.get_match_infos()

    # View.ask_for_report_choice()

    # View.display_boot_menu()
    # finish = View.finish_to_register_players_in_club()
    # View.display_winner()
    # View.display_club_players()

