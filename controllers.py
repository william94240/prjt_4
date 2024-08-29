"""Ce module contient le controleur de l'application."""

import random

from models import Tournament, Player, Round, Match
from views import View


class Controller:
    """Le controleur
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

            # Quitter
            elif user_choice == "4":
                exit()

    @classmethod
    def get_club_player(cls):
        """Inscrit un joueur au club.

        Returns:
            None.
        """

        while True:
            player_data = View.ask_for_player_infos()
            chess_id = player_data[2]
            if Player.chess_id_exist(chess_id):
                player = Player.chess_id_exist(chess_id)
                response = View.chess_id_exist(player)
                if response:
                    # delete the player et continuer la saisie
                    cls.delete_player(chess_id)
            player = Player(*player_data)
            View.display_player(player)
            player.save_club_player()
            finish = View.finish_to_register_players_in_club()
            if finish != "o":
                break

    # @staticmethod
    # def chess_id_exist(chess_id):
    #     return Player.chess_id_exist(chess_id)

    @staticmethod
    def delete_player(chess_id):
        Player.delete_player(chess_id)

    @classmethod
    def create_a_tournament(cls):
        """
        Creation d'un tournoi

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

        for i in range(0, nb_round):
            round_name = f"Round {i + 1}"
            round = Round(round_name)

            if round_name == "Round 1":
                # Au premier tour, mélanger directement les joueurs.
                random.shuffle(players)

            else:
                # Pour les autres tours, trier les joueurs par score_total.
                players = sorted(
                    players,
                    key=lambda x: x.score_total,
                    reverse=True
                                )

            matches_round = []
            for j in range(0, len(players), 2):
                player_1 = players[j]
                player_2 = players[j+1]
                match = Match(
                    player_1,
                    player_2
                            )
                matches_round.append(match)
                round.matches.extend(matches_round)

            View.go_on_matches(round_name)
            View.display_round_matches(matches_round)

            response = View.want_enter_the_scores_of_the_matches()
            if response == "o":
                cls.get_display_scores(round_name, matches_round)
            else:
                exit()

            round.round_finished()
            tournament.rounds.append(round)
            tournament.save_tournament()  # --------------> Sauvegarde le tournoi.

        winner = tournament.whos_won()
        View.display_winner(winner)
        tournament.tournament_finished()
        tournament.save_tournament()  # --------------> Sauvegarde le tournoi.

        return tournament

    @staticmethod
    def tournament_name_exist(name_tournament):
        return Tournament.tournament_name_exist(name_tournament)

    @classmethod
    def register_tournament_player(cls, tournament: Tournament):
        """Saisie un joueur pour le tournoi.

        Returns:
            None.
         """
        tournament.nb_player = View.ask_number_of_players()

        for i in range(0, tournament.nb_player):
            player_data = View.ask_for_player_infos()
            player = Player(*player_data)
            chess_id = player_data[2]
            player_exist = Player.chess_id_exist(chess_id)

            if player_exist:
                player_redefinition = View.chess_id_exist(player_exist)
                if player_redefinition:
                    # delete the player et continuer la saisie
                    cls.delete_player(chess_id)

                else:
                    # delete the player et le resaisir
                    cls.delete_player(chess_id)
                    player = player_exist

            View.display_player(player)
            tournament.players.append(player)
            # Sauvegarde également le joueur dans le club.
            player.save_club_player()
            tournament.save_tournament()  # --------------> Sauvegarde le tournoi.

    @staticmethod
    def get_display_scores(round_name, matches_round):
        """
        Crée des paires pour les matchs et permet la saisie des scores et
        l'affichage des matchs du round.
        """
        for k, match in enumerate(matches_round):
            match.player_1.score = View.set_player_score(
                match.player_1.first_name, match.player_1.last_name)
            if match.player_1.score == 1:
                match.player_2.score = 0

            elif match.player_1.score == 0.5:
                match.player_2.score = 0.5

            elif match.player_1.score == 0:
                match.player_2.score = 1

            match.player_1.score_total += match.player_1.score
            match.player_2.score_total += match.player_2.score

            score = (
                f"Le/La joueur(euse) ---> {match.player_1.first_name} "
                f"{match.player_1.last_name} a "
                f"un score sur le match = {match.player_1.score}\n"
                f"et "
                f"un score cumulé = {match.player_1.score_total}\n\n"

                f"Le/La joueur(euse) ---> {match.player_2.first_name} "
                f"{match.player_2.last_name} a "
                f"un score sur le match = {match.player_2.score}\n"
                f"et "
                f"un score cumulé = {match.player_2.score_total}\n\n"
                    )

            View.display_score(round_name, k,  score)

    @classmethod
    def resume_tournament(cls):
        """Reprendre un tournoi non incomplet.
        """
        tournament = Tournament.extract_tournament()
        if tournament.nb_round_in_progress < tournament.nb_round:
            if tournament.nb_player_in_progress < tournament.nb_player:
            cls.register_tournament_player(tournament)
            View.go_on_tournament()
            players = tournament.players
            nb_round = tournament.nb_round

            for i in range(Tournament.nb_round_in_progress, nb_round):
                round_name = f"Round {i + 1}"
                round = Round(round_name)

                if round_name == "Round 1":
                    # Au premier tour, mélanger directement les joueurs.
                    random.shuffle(players)

                else:
                    # Pour les autres tours, trier les joueurs par score_total.
                    players = sorted(
                        players,
                        key=lambda x: x.score_total,
                        reverse=True
                                    )

                matches_round = []
                for j in range(0, len(players), 2):
                    player_1 = players[j]
                    player_2 = players[j+1]
                    match = Match(
                        player_1,
                        player_2
                                )
                    matches_round.append(match)
                    round.matches.extend(matches_round)

                View.go_on_matches(round_name)
                View.display_round_matches(matches_round)

                response = View.want_enter_the_scores_of_the_matches()
                if response == "o":
                    cls.get_display_scores(round_name, matches_round)
                else:
                    exit()

                round.round_finished()
                tournament.rounds.append(round)
                tournament.save_tournament()

    @staticmethod
    def generate_report():
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
            # Rechercher un tournoi spécifique et Affiche les informations
            #  qui lui sont associées.
            name_tournament = View.search_a_specific_tournament_name()
            args = Tournament.search_a_specific_tournament_informations(
                name_tournament)
            View.display_tournament_informations(*args)

        elif report_choice == "4":
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
    # Controller.create_a_tournament()
    # Controller.delete_player("kkk")

    print(Controller.tournament_name_exist("Hay"))
