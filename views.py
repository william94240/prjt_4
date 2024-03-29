

class View:

    # MENU DEMARRER

    @classmethod
    def display_boot_menu(cls, message):
        print(message)

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

        name_tournament = input("Entrez le Nom du tournoi: ")
        location = input("Entrez le lieu du tournoi: ")
        start_date = input("Entrez la date de début du tournoi: ")
        end_date = input("Entrez la date de fin du tournoi: ")
        nb_round = int(input("Entrez le nombre de tour du tournoi: "))
        description = input("Entrez la description du tournoi: ")
        # tournament_infos = (name_tournament, location,
        #                     start_date, end_date, nb_round, description)

        return name_tournament, location, start_date, end_date, nb_round, description

    @classmethod
    def display_tournament(cls, tournament):
        print("Tournoi -->", tournament)

    def ask_for_player_infos(self):
        """
            Demande d'infos,sur le joueur.

            Returns:
                tuple: un tuple d'infos
        """
        first_name = input("Entrez le prénom du joueur: ")
        last_name = input("Entrez le nom du joueur: ")
        birthday = input("Entrez la date de naissance du joueur: ")
        chess_id = input("Entrez l'dentifiant Echecs: ")
        player_data = {"first_name": first_name, "last_name": last_name,
                       "birthday": birthday, "chess_id": chess_id}

        return player_data

    def display_player(self, player):
        """Affiche le joueur.

            Args:
                joueur (_type_): _description_
        """
        print("Player: ", player)

    def get_match_infos(self):
        """
        Demande d'infos à saisir sur le match.

        Returns:
            : un tuple d'infos
        """

        player_1 = self.ask_for_player_infos()
        score_player_1 = int(
            input("Résultat du joueur 1 entre (0, 0.5, 1): "))
        player_2 = self.ask_for_player_infos()
        score_player_2 = int(
            input("Résultat du joueur 2 entre (0, 0.5, 1): "))
        match_data = (player_1, player_2, score_player_1, score_player_2)
        return match_data

    def display_match(self, match):
        """Affiche le joueur.

        Args:
            Match: Les composantes d'un match
        """
        print("Match -->", match)


# if __name__ == "__main__":
#     view = View()
#     # view.ask_for_player_infos()
#     view.get_match_infos()
