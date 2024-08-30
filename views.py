import dateparser
import rich
from rich.prompt import Prompt
import re
from datetime import datetime


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
                              3 - Reprendre un tournoi.
                              4 - Génération des rapports.
                              5 - Quitter.
                           """

        rich.print(display_message)
        user_choice = cls.user_input()
        return user_choice

    @staticmethod
    def user_input():
        """Demande le choix de l'utilisateur."""
        while True:
            choice = Prompt.ask("Votre choix ", default="2")
            if choice in ["1", "2", "3", "4", "5"]:
                return choice
            else:
                rich.print(f"'{choice}' n'est pas valide.Veuillez effectuer un choix dans (1, 2, 3, 4, 5)")

    @staticmethod
    def ask_for_player_infos():
        """
            Demande les infos sur le joueur.

            Returns:
                tuple: un tuple d'infos
        """

        rich.print("-" * 100)

        while True:
            chess_id = Prompt.ask("Entrer l'identifiant Echecs ")
            regex_chess_id = r"^[A-Z]{2}[0-9]{5}$"
            regex_chess_id_compile = re.compile(regex_chess_id)

            if (re.match(regex_chess_id_compile, chess_id)):
                break
            else:
                rich.print(
                    f"le format de {chess_id} n'est pas conforme"
                    f" à l'identifiant national d’échecs: ex. type: AB12345"
                    )

        while True:
            first_name = Prompt.ask("Entrer le prénom du joueur ")
            regex_first_name = r"^[A-Za-z &'-éè`àùç\^\']+$"
            regex_first_name_compile = re.compile(regex_first_name)

            if (re.match(regex_first_name_compile, first_name)):
                break
            else:
                rich.print(
                    f"le format de '{first_name}' n'est pas conforme"
                    f" au prénom: ex. type: Jean, Jean-Charles..."
                    )

        while True:
            last_name = Prompt.ask("Entrer le nom du joueur ")
            regex_last_name = r"^[A-Za-z &'-éè`àùç\^\']+$"
            regex_last_name_compile = re.compile(regex_last_name)

            if (re.match(regex_last_name_compile, last_name)):
                break
            else:
                rich.print(
                    f"le format de '{last_name}' n'est pas conforme"
                    f" au nom: ex. type: Mounier, Moulin-Molinarie..."
                    )

        while True:
            entry = Prompt.ask("Entrer la date de naissance du joueur ")
            birthday = dateparser.parse(entry)
            if birthday is not None:
                break
            rich.print(
                    f"le format de date '{entry}' n'est pas conforme"
                    f" aux formats prédéfinis: ex. type: 1990-01-01,"
                    f" 01/01/1990,  lundi, mardi, aujourd'hui, demain,"
                    f" 30 juillet 2021, 30 juillet 21 ..."
                    )

        return (first_name,
                last_name,
                chess_id,
                birthday
                )

    @staticmethod
    def chess_id_exist(player):
        """message si l'identifiant existe déjà.
        """
        rich.print(f"Le joueur:\n\n{player}\nExiste déjà.")
        rich.print("Voulez-vous redéfinir le joueur ?")
        response = Prompt.ask("o/n ", default="o")
        if response == "o":
            # delete the player et continuer la saisie
            return True


    @staticmethod
    def display_player(player):
        """Affiche le joueur.
        """
        rich.print("-" * 100)
        rich.print(player)

    @staticmethod
    def finish_to_register_players_in_club():
        """Vérifie si l'inscription des jouers est terminée.
        """
        finish = Prompt.ask("voulez-vous inscrire un joueur ? (o/n) ", default="o")
        return finish

    @staticmethod
    def request_tournament_infos():
        """
        Demande d'infos,sur le tounoi.

        Returns:
            tuple: un tuple d'infos

        """

        rich.print("-" * 100)

        from controllers import Controller

        while True:
            name_tournament = Prompt.ask("Entrer le nom du tournoi ")
            regex_name_tournament = r"^[A-Za-z0-9 !\"#\$%&'\(\)*+-éè`àùç/:<=>@\\\^_~\"\'\|\./§]+$"
            regex_name_tournament_compile = re.compile(regex_name_tournament)
            if (re.match(regex_name_tournament_compile, name_tournament)):
                tournament_name_exist = Controller.tournament_name_exist(name_tournament)
                if not tournament_name_exist:
                    break
                else:
                    rich.print(tournament_name_exist)
                    rich.print("Vous devez saisir un nouveau nom de tournoi.")
                    continue
            else:
                rich.print(
                    f"le format de {name_tournament} n'est pas conforme"
                    f" au nom du tournoi: ex. type: Tournoi de Paris #1,"
                    f" Tournoi de Lyon(parilly)..."
                    )

        while True:
            location = Prompt.ask("Entrer le lieu du tournoi ")
            regex_location = r"^[A-Za-z0-9 #&'\(\),-éè`àùç/:@\\\^_~\"\'\./§]+$"
            regex_location_compile = re.compile(regex_location)
            if (re.match(regex_location_compile, location)):
                break
            else:
                rich.print(
                    f"le format de '{location}' n'est pas conforme"
                    f" au nom du lieu du tournoi: ex. type: Paris, Lyon..."
                    )

        while True:
            entry = Prompt.ask(
                """
                Entrer la date de début du tournoi
                - si vous ne saisisez rien, la date en cours sera
                considerez comme date de début du tournoi
                """,
                default=datetime.now().strftime("%Y-%m-%d")
                                )

            start_date = dateparser.parse(entry)
            if start_date is not None:
                break
            else:
                rich.print(
                    f"le format de date '{entry}' n'est pas conforme"
                    f" aux formats prédéfinis: ex. type: 1990-01-01,"
                    f" 01/01/1990,  lundi, mardi, aujourd'hui, demain,"
                    f" 30 juillet 2021, 30 juillet 21 ..."
                            )
                # response = input(
                #     "Voulez-vous que la date d'aujourd'hui soit considéreé comme date de début du tournoi ? (o/n): "
                #                 )
                # if response == "o":
                #     # Prendre la date en cours pour date de début du tournoi.
                #     start_date = datetime.now()
                #     break

        while True:
            entry = Prompt.ask(
                """
                Entrer la date de fin du tournoi
                -si vous ne saisisez rien, la date en cours sera
                considerez comme date de fin du tournoi
                """,
                default=datetime.now().strftime("%Y-%m-%d")
                        )

            end_date = dateparser.parse(entry)
            if end_date is not None:
                break
            else:
                rich.print(
                    f"le format de date {entry} n'est pas conforme"
                    f" aux formats prédéfinis: ex. type: 1990-01-01,"
                    f" 01/01/1990,  lundi, mardi, aujourd'hui, demain,"
                    f" 30 juillet 2021, 30 juillet 21 ..."
                    )
                # response = input(
                #     "Voulez-vous que la date d'aujourd'hui soit considéreé comme date de fin du tournoi ? (o/n): "
                #                 )
                # if response == "o":
                #     # Prendre la date en cours pour date de fin du tournoi.
                #     end_date = datetime.now()
                #     break

        while True:
            nb_round = Prompt.ask("Entrer le nombre de tour du tournoi ", default="4")
            if nb_round.isdigit():
                nb_round = int(nb_round)
                break
            else:
                rich.print(
                    f"'{nb_round}' n'est pas un nombre entier."
                    f" Le nombre de tour du tournoi doivent être de type: 4, 5, 6...")

        description = Prompt.ask("Entrer la description du tournoi ", default="R.a.s")

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
        while True:
            try:
                number_of_players = int(Prompt.ask(
                    "Combien des joueurs voulez-vous ajouter au tournoi ?"
                                                    )
                                        )
                if number_of_players and number_of_players % 2 == 0:
                    print(number_of_players)
                    return number_of_players
                else:
                    rich.print("Veuillez entrer un nombre pair de joueurs")
                    continue
            except ValueError:
                rich.print("Veuillez entrer un nombre pair de joueurs")

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
        for k, match_round in enumerate(matches_round):
            rich.print(f"Match {k+1}>>>>>>")
            rich.print(match_round)

    @staticmethod
    def want_enter_the_scores_of_the_matches():
        """Demande si vous voulez saisir les scores des matchs."""
        rich.print("-" * 100)
        response = Prompt.ask("Voulez-vous saisir les scores des matchs ?(o/n) ", default="o")
        rich.print("")
        return response

    @staticmethod
    def set_player_score(player_1_first_name, player_1_last_name, player_2_first_name, player_2_last_name):
        """
        Demande le score du jouer.

        Returns:
            : le score du jouer
        """
        while True:
            score_player = Prompt.ask(
                f"""
                Qui a gagné :
                1. {player_1_first_name} {player_1_last_name}
                2. {player_2_first_name} {player_2_last_name}
                3. Match nul
                """
                                    )
            if score_player == "1":
                player_1_score = 1
                player_2_score = 0
                return player_1_score, player_2_score
            elif score_player == "2":
                player_1_score = 0
                player_2_score = 1
                return player_1_score, player_2_score
            elif score_player == "3":
                player_1_score = 0.5
                player_2_score = 0.5
                return player_1_score, player_2_score
            else:
                rich.print("veuillez effectuer un choix valide dans (1, 2, 3)")
        # while True:
        #     score_player = Prompt.ask(
        #         f"""
        #         Entrer le résultat de '{player_1_first_name} {player_1_last_name}' CONTRE '{player_2_first_name} {player_2_last_name}'
        #         [La valeur doit être comprise entre (0, 0.5, 1)]
        #         """
        #                             )
        #     if score_player in ["0", "0.5", "1"]:
        #         score_player = float(score_player)
        #         return score_player
        #     else:
        #         rich.print("veuillez entrer un chiffre valide compris dans [0, 0.5, 1]")

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
        rich.print("*" * 100)
        rich.print("La liste des resultats du tournoi suivant l'ordre "
                   "décroissant des scores est:\n"
                   )
        for player in winner:
            rich.print(player)
            rich.print("-" * 100)

        rich.print(f"***** Le Vainqeur du tournoi est: *****\n{winner[0]}")

    @staticmethod
    def game_over():
        """Affiche la fin du tournoi."""
        rich.print("Fin du tournoi")

    @staticmethod
    def message_resume(tournament):
        """Affiche le message de  reprise."""
        rich.print(f"Nous reprenons le tournoi: {tournament}.")

    @staticmethod
    def message_no_resume():
        """Affiche le message de non reprise."""
        rich.print("Ce tournoi est déjà terminé.")

    @staticmethod
    def ask_for_report_choice():
        """Demande le choix du rapport à afficher."""
        display_message = """Quel rapport souhaitez-vous obtenir ?
                           1 - Afficher la liste de tous les joueurs inscrits
                               au club.
                           2 - Afficher la liste des tournois dejà orgnanisés.
                           3 - Rechercher un tournoi spécifique et Afficher
                               les informations associées.
                           4 - Quitter
                           """

        rich.print(display_message)
        report_choice = Prompt.ask("Votre choix ", default="2")
        return report_choice

    @staticmethod
    def display_club_players(players):
        """Affiche les joueurs du club."""
        rich.print("-" * 100)
        rich.print()
        rich.print("Liste de tous les joueurs inscrits à notre club: ")
        rich.print()
        for player in players:
            rich.print(player)
            rich.print("-"*50)

    @staticmethod
    def display_list_of_tournament(list_of_tournaments):
        """Affiche la liste des tournois déjà organisés par le club."""
        rich.print("*" * 100)
        rich.print("Liste des tournois déjà organisés par le club: \n")
        for tournament in list_of_tournaments:
            rich.print(tournament)
            rich.print("-"*50)

    @staticmethod
    def search_a_specific_tournament_name():
        """Demande le nom du tournoi à rechercher."""
        name_tournament = Prompt.ask("Entrer le nom du tournoi ")

        return name_tournament

    @staticmethod
    def display_tournament_informations(
            tournament, players, rounds, round_matches
                                        ):
        """Affiche les informations du tournoi."""
        rich.print("*" * 100)
        rich.print(f"Les informations sur le tournoi \"{tournament.name_tournament}\": --->\n")
        rich.print(tournament)
        rich.print("*" * 100)
        rich.print(f"Les joueurs participants au tournoi \"{tournament.name_tournament}\": --->:\n")
        for player in players:
            rich.print(player)
            rich.print("-" * 30)
        rich.print("*" * 100)
        rich.print(f"Les rounds organisés dans le tournoi \"{tournament.name_tournament}\": --->\n")
        for round in rounds:
            rich.print(round)
            rich.print("-" * 30)
        rich.print("*" * 100)
        rich.print("Les matchs composants les rounds: --->\n")
        for round_match in round_matches:
            rich.print(round_match[0])
            rich.print("-" * 30)
            for i, match in enumerate(round_match[1]):
                rich.print(f"Match {i+1}>>>>>>\n")
                rich.print(match)
                rich.print("-" * 30)


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
    # View.user_input()

    # View.ask_for_player_infos()
    # print(View.request_tournament_infos())
    # print(View.ask_number_of_players())
    # View.user_input()
    # print(View.set_player_score("william", "Mopete"))
    # View.ask_number_of_players()
    View.message_resume("name_tournament")
