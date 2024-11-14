# 2024_2025__p04_projet1_gp6
Jules Bock
Maxime Bourgain
Adrien Baroux-Arbona

# Présentation PPT : https://lndb92-my.sharepoint.com/:p:/g/personal/jul_bock_lndb_eu/EVLR637XVYtBpLN8QqtaxiABl4XP3RwcP-KqQsUkZCA94A?e=T2FI9X

Enoncé :

SUJET : binaire, décimal, hexadécimal vers binaire, décimal, hexadécimal

       On considère les nombres entiers écrits en base 2, 10 et 16.
       Ecrire un programme qui permet de passer de l'écriture d'un entier dans
       une des bases (2, 10 ou 16) à l'écriture de cet entier dans une des bases
       (2, 10 ou 16).
       
       Vous serez évalués suivant les 6 critères décrits dans le fichier excel de nom
       "notation__projets_nsi__p01_et_p04__2024_2025.xlsx" et qui sont désignés par:
 
       1. Documentation claire
       2. Lisibilité du code
       3. Run (exécution du programme)
       4. Présentation (...du projet devant la classe)
       5. Architecture (organisations des dossiers et fichiers)
       6. IA génératives (interactions avec les IA génératives)

REMARQUE : Vous n'utiliserez pas les éventuelles fonctions déjà disponibles dans python,
       pour passer d'une base à une autre.


Explication de notre projet:
I  main.py

Nous avons d'abord décidé que le programme principal serait simplement stocké dans le fichier main.py. 
La fonction principale du programme run_main y est lancé. Cette fonction use deux autres focntions (execute_convertion_and_give_result et ask_for_restart) respectivement définies dans les fichier tools_main.py et main.py.

La fonction ask_for_restart redemande à l'utilisateur s'il veut réutiliser la fonction principale. Lorsque la réponse est positive, la fonction run_main est relancée tandis que si la réponse est négative, le porgrammme est arrêté. 

II dossier tools

Nous avons crée plusieurs fichiers tools qui contiennent les différentes fonctions de notre programme (sauf ask_for_restart et run_main qui se trouve dans le fichier 
main.py): 

       a. __init__.py

Ce fichier permet de centraliser les imports afin de les faciliter et de n'avoir besoin d'écrire qu'une seule ligne pour tout importer.

       b. tools_ask_for.py


Comme son nom l'indique ce fichier stocke les différentes fonctions qui demandent des informations à l'utilisateur (ask_for_init_number, ask_for_init_base, ask_for_target_base)

       c. tools_convert.py

Ce fichier stocke les différentes fonctions qui permettent de convertir le nombre de la base donnée en la base demandée (il y a 3 bases disponibles : 2, 10, 16). De plus, un dictionnaire est présent dans la fonction. Il assigne à chaque fonction de conversion, les bases d'origine et finale, qui y correspondent. 

       d. tools_side.py

Ce fichier contient les fonctions qui permettent la vérification de la validité des bases et nombres entrés par l'utilisateur de notre programme.
Par ailleurs, la variable answer y est définie, pour son usage par la fonction ask_for_restart.


IV data.py

Enfin, le fichier data.py contient la presque totalité des variables évoquées dans les différents fichiers constitiants du projet. Les variables des fonctions d'intéractions avec l'utilisateur mais aussi les listes des différentes bases utilisées. 


Post-Scritum:
Nous tenons à préciser que nous avons choisi de travailler avec des brouillons personnels afin de ne pas créer de conflits dans les fichiers majeurs. Ces brouillons étaient respectivement nommés brouillon_adrien.py, brouillon_jules.py et brouillon_max.py. De plus, un fichier gitignore a été utilisé.






Ce fichier contient la majorité des fonctions du projet. En effet, tous les fonctions de conversion des différentes bases y sont présentes. 
Ces mêmes fonctions importent des variables provenant de data.py, principalement des chaînes de caractères ou des listes. 
De plus, un dictionnaire est présent dans la fonction. Il assigne à chaque fonction de conversion, les bases d'origine et finale, qui y correspondent. 

De surcroît, tools_main contient de même de nombreuses fonctions d'exécution du programme. Les fonctions secondaires de demande du nombre, de la base d'origine et de la base finale utilisent elles aussi des variables présentes dans data.py. 
Enfin, les fonctions principales de notre projet (execute_convertion_and_give_result et give_result) sont présentes dans ce même fichier et sont initiées avant d'être utilisées par la fonction run_main évoquée précédemment. 