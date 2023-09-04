# Projet 10 OpenClassRoom : Créez une API sécurisée RESTful en utilisant Django REST
## Présentation du projet
Le but de ce projet est de créer une API REST permettant de gérer des projets , des tâches et d'ajouter des commentaires.
Cet API permet également de créer des users , de donner les droits d'accès à ces users.

## composition
Tous les fichiers .py necessaires au fonctionnement du logiciel se trouvent dans le répertoire src.
Les autres fichiers sont :
- README.md qui contient des informations sur le logiciel
- requirements.txt contient les packages necessaires au bon fonctionnement du logiciel
- tox.ini permet de paramétrer flake8 pour voir si le programme répond aux normes pep8

## Installation de l'application
- Cloner le dépôt de code à l'aide de la commande `https://github.com/Jean-PierreBE/SoftDesk.git`
- Rendez-vous depuis un terminal à la racine du répertoire SoftDesk avec la commande `cd SoftDesk`
- Créer un environnement virtuel pour le projet avec `$ python -m venv env` sous windows ou `$ python3 -m venv env` sous macos ou linux.
- Activez l'environnement virtuel avec `$ env\Scripts\activate` sous windows ou `$ source env/bin/activate` sous macos ou linux.
- installer les packages python du fichier requirements.txt en lançant la commande suivante 
  - `pip install -r requirements.txt`

les packages installés sont les suivants :
- django : framework permettant de développer les sites webs
- djangorestframework : framework permettant de décvelopper des apis

## Lancement du programme
On lance le programme en tapant sur la ligne de commande dans le répertoire src:
- `python manage.py runserver`

## Déroulement du programme
Une fois la commande précédente exécutée, mettre l'adresse suivante
- `http://127.0.0.1:8000/`
dans le browser de votre choix.
- pour commencer il faut créer un user avec le end point signup. Il faut renseigner au minimum un user , adresse mail et password.
- une fois le user créé , on peut se connecter avec le end point login avec le user et le password. L'API renverra un code token.
  Avec ce code token on peut utiliser l'API.  
- L'utilsateur pourra commencer à créer un projet , il sera le creator. Une fois le projet créé , d'autres utilisateurs pourront s'ajouter au projet avec des postes divers mais pas creator. 
- Si l'utilisateur est lié à un projet , il peut créer une issue   


## Contrôle qualité
Pour vérifier la qualité du code , on peut lancer la commande suivante :
- `flake8 --format=html --htmldir=flake-report src`
Le rapport sortira en format html dans le répertoire flake-report

pour cela il faut installer :
- flake8 : contrôle du code pour vérifier la compatibilité avec les normes pep8
- flake8-html : permet de sortir le rapport flake8 sous format html
- flake8-functions : permet d'ajouter des contrôles au niveau des fonctions (ex : longueur maximale des fonctions)

le fichier tox.ini contient la configuration pour flake8.
- `exclude = migrations` : la longueur maximale de chaque ligne ne peut pas dépasser 119 caractères
- `max-line-length = 120` : la longueur maximale de chaque ligne ne peut pas dépasser 119 caractères
- `max-function-length = 50` : la longueur maximale de chaque fonction ne peut pas dépasser 50 lignes
- `ignore = CFQ002, CFQ004, W503, W504` : évite les erreurs
  - CFQ002 : nombre d'arguments en entrée trop élevés (> 6)
  - CFQ004 : nombre d'éléments en retour trop élevés (> 3)
  - W503 : saut de ligne avant un opérateur
  - W504 : saut de ligne après un opérateur

Ces paramètres peuvent être modifiés
