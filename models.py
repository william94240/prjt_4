class Player:
    """
    Le joueur.
    """

    def __init__(self, first_name: str, last_name: str, birthday: str,
                 chess_id: str):
        """Création du joueur.
        Args:
            nom (str): le nom du joueur à créer.
            prenom (str): le prenom du joueur à créer.
            date_naissance (date): la date_naissance du joueur à créer.
            identifiant_echecs (str): l'identifiant nationale d'echecs
            du joueur à créer.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.chess_id = chess_id
        self.points = 0.0  # Initialiser les points du joueur à 0
        self.joueurs = []

    def __repr__(self) -> str:
        """Méthode pour afficher les détails du joueur

        Returns:
            str: affiche les details sur le joueur.
        """

        return f"Prénom: {self.first_name} :: Nom: {self.last_name} :: Date de naissance: {
            self.birthday} :: Identifiant echecs: {self.chess_id}"

    def get_player_in_dictionnary_format(self):
        """
        Transforme les données en dictionnaire

        Returns:
            Dict: données en Dictionnaire
        """
        player_dictionnary = {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birthday": self.birthday,
            "chess_id": self.chess_id,
        }

        return player_dictionnary


class Tournament:

    """Le tournoi.
    """

    def __init__(self, name_tournament: str, location: str, start_date: str, end_date: str,
                 nb_round: int = 4, description: str = ""):
        """Creation Tournoi.

        Args:
            name_tournament (str): Le nom du tournoi
            location (str): Le lieu du tournoi
            start_date (datetime): La date de début du tournoi
            end_date (datetime): La date de fin du tournoi
            nb_round (int, optional): Le nombre de tours du tournoi. Defaults to 4.
            description (str, optional): La description du tournoi. Defaults to "".
        """
        self.name_tournament = name_tournament
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.nb_round = nb_round
        self.description = description
        self.rounds = []
        self.tournaments = []
        # Liste pour stocker les joueurs inscrits
        self.players_registered = []

        # le numéro correspondant au tour actuel manque, à ajouter.

    def __repr__(self):
        """
        Méthode pour afficher les détails sur tournoi
        """

        return f"Nom du tournoi: {self.name_tournament} ** Lieu: {self.location} ** Date début: {self.start_date} ** Date fin: {self.end_date} ** Tours: {self.nb_round}  ** Description: {self.description}"


class Match:
    """
    Le Match.
    """

    def __init__(self, player_1: Player, player_2: Player, score_player_1: int = 0,  score_player_2: int = 0):
        """Création de l'entité Match.

        Args:
            player_1 (Joueur): Le premier joueur.
            player_2 (Joueur): Le second  joueur.
        """
        self.player_1 = player_1
        self.player_2 = player_2
        # Peut être rédefinit plus tard lors de la saisie des résultats
        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2

    def definir_resultat(self, score_player_1: int = 0, score_player_2: int = 0):
        """
        Méthode pour définir le résultat du match

        Args:
            resultat (Tuple): Le resultat
        """
        self.resultat = (score_player_1, score_player_2)

    def obtenir_resultat(self):
        """
        Méthode pour obtenir les résultats du match

        Returns:
            str: Retour des points de deux joueurs.
        """

        return self.resultat

    def __repr__(self):
        """
        Méthode pour afficher les détails du match
        """
        return f"Joueur 1: {self.player_1} - point: {self.score_player_1} ::: Joueur 2: {self.player_2} - point: {self.score_player_2}"


class Round:
    """ Création de l'entité Round."""
