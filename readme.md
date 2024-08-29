# OpenClassrooms Projet 4 - Gestionnaire de Tournoi d'échecs
Ce programme Concue sous Python, est destiné à aider les clubs d'échecs à gérer leurs tournois hors ligne et à générer des rapports. Sa programmation repose sur le Design Pattern MVC (Modèle Vue Contrôleur). Le programme peut être interrompu en cours de compétition pour être repris par la suite.
_Il a été Developpé sous Windows 11 - Python version 3.12.4_
## Installation:
En préliminaire installer Python.
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
* Windows:
 ```
    /env/Scripts/activate
 ```
* Linux:
```
    source env/bin/activate
```
A l'aide de pip installer les dépendances requises:
```
pip install -r requirements.txt
```
Démarrer l'application avec la commande suivante:
```
python main.py
```

## Les options d'utilisation
### 1) Créer un tournoi
* Le programme vous permet de gérer des tournois d'échecs. Lors de la première utilisation, sélectionnez "Créer un tournoi", puis laissez vous guider.
* Si aucun joueurs n'est présent dans la base de donnée, vous serez invité à en créer.
* Lors d'un tournoi, vous serez invité à rentrer les résultats après chaque match. A la fin d'un tournoi, un classement sera généré.
* Pendant le tournoi, vous aurez la possibilité de sauvegarder le tournoi en cours, en charger un nouveau, de voir ou modifier les classements.
### 2) Charger un tournoi
* Cette section vous permet de charger un tournoi depuis la base de donnée.
* Une fois le tournoi chargé, vous serez invité à le continuer.
### 3) Créer des joueurs
* Lorsque vous sélectionnez cette option, vous êtes invité à rentrer le nombre de joueurs à créer.
* Laissez vous ensuite guider par le programme.
### 4) Les rapports
* Cette section vous permet de générer différents rapport.
* Vous pouvez consulter: le classement global des joueurs par classement et ordre alphabétique.
* Les détails des tournois passés: classement des joueurs du tournoi, tours et matchs de chaque tournois.
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
