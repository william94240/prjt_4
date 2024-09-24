# OpenClassrooms Projet 4 - Gestionnaire de Tournoi d'échecs
Ce programme Concu sous Python, est destiné à aider les clubs d'échecs à gérer leurs tournois hors ligne et à générer des rapports. Sa programmation repose sur le Design Pattern MVC (Modèle Vue Contrôleur). Le programme peut être interrompu en cours de compétition pour être repris par la suite.
_Il a été Developpé sous Windows 11 - Python version 3.12.4_
## Installation:
En préliminaire, installer Python.
Lancez la console et placez vous dans le dossier d'installation cible de votre choix puis clonez ce repository:

> git clone https://github.com/william94240/prjt_4.git

Par la suite, installer le module Virtualenv de manière suivante:
````
python -m pip install virtualenv
````
Réplacez-vous dans votre dossier d'installation, puis créez un nouvel environnement virtuel à l'aide de Virtualenv:
```
python -m venv env
```
Activez-le.
* Pour Windows:
 ```
    /env/Scripts/activate
 ```
* Pour Linux:
```
    source env/bin/activate
```
A l'aide de pip, installer les dépendances requises:
```
pip install -r requirements.txt
```
Démarrer l'application avec la commande suivante:
```
python main.py
```

## Les Différentes options d'utilisation.
### 1] Ajouter un(des) joueur(s) au club
- Cette option a pour vocation de créer et d'enregistrer des joueurs dans la base de données du club.
- Laissez-vous ensuite guider par le programme.
### 2] Créer et démarrer un tournoi.
- Cette option est dédiée à la création d'un tournoi.
- En premier, vous êtes convié à saisir les noms des joueurs participants. Dans l'éventualité où le joueur existe dans la base de données du club, il vous sera demandé de le confirmer, dans le cas contraire vous serez invité à le redéfinir.
- Lors d'un tournoi, vous serez invité à rentrer les résultats après chaque match. A la fin d'un tournoi, un classement sera automatiquement généré et Le nom du Vainqueur d'affichera.
- Il est à noter que la sauvegarde du tournoi s'effectue en permanence de manière automatique afin de garantir la persistance des données.
### 3] Reprendre un tournoi.
- Cette option permet la reprise d’un tournoi incomplet.
- Concrètement, elle permet d'extraire un tournoi dans son état avant interruption depuis la base de données. Une fois qu’elle est extraite, vous serez convié à le continuer.
### 4] Génération des rapports.
- Cette option permet d'éditer toutes sortes des rapports :
    > - Afficher la liste triée de tous les joueurs au club
    > - Afficher la liste triée de tournois déjà orgnanisés avec les détails inhérents : les joueurs, les tours et les matcorganiséshs de chaque tournois.
    > - Rechercher un tournoi spécifique et afficher les informations associées.
### 5) Générer le rapport Flake8
* Ouvrer le terminal saisisez:
```
pip intall flake8-html
```
* Créer également un fichier `.flake`
* Ecrire dedans le texte suivant:
```
[flake8]
exclude = .git, env, __pycache__, .gitignore
max-line-length = 119
```
* Pour générer le rapport flake8 au format HTML tapez la commande suivante:
```
flake8 --format=html --htmldir=flake-report
```
* Vous trouverez dans le dossier `flake_report` les rapports de flake8

