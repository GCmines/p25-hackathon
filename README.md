FAIRE CTRL+SHIFT+V si le markdown apparaît sans mise en forme
# EXPLICATIONS

## LANCER LA SIMULATION

Exécuter le programme main.py pour lancer la simulation.

## PARAMETRES MODIFIABLES :

|DESCRIPTION                                         |   Nom de la variable              |   Valeur par défaut |
|---|---|:-:|
|La taille de la grille de simulation                |   GRID_SIZE                       |   30|
|L'énergie initiale des moutons                      |   SHEEP_INITIAL_ENERGY            |   20|
|L'énergie initiale des loups                        |   WOLF_INITIAL_ENERGY             |   40 |
|L'énergie perdue par un mouton dans un tour         |   SHEEP_ENERGY_LOSS_PER_TURN      |   1|
|L'énergie perdue par un loup dans un tour           |   WOLF_ENERGY_LOSS_PER_TURN       |   2|
|Le coût énergétique de la reproduction              |   REPRODUCTION_ENERGY_COST        |   20|
|Le seuil énergétique de reproduction des moutons    |   SHEEP_REPRODUCTION_THRESHOLD    |   50|
|Le seuil énergétique de reproduction des loups      |   WOLF_REPRODUCTION_THRESHOLD     |   80|
|Le gain énergétique de l'herbe pour les moutons     |   SHEEP_ENERGY_FROM_GRASS         |   15|
|Le gain énergétique des moutons pour les loups      |   WOLF_ENERGY_FROM_SHEEP          |   35|
|La limite d'âge des moutons                         |   SHEEP_MAX_AGE                   |   50|
|La limite d'âge des loups                           |   WOLF_MAX_AGE                    |   40|
|Le nombre de moutons à l'initialisation             |   NB_SHEEP_INIT                   |   50|
|Le nombre de loups à l'initialisation               |   NB_WOLVES_INIT                  |   10|
|La proportion d'herbe à l'initialisation            |   INITIAL_GRASS_COVERAGE          |   0.3|
|Le temps de repousse de l'herbe                     |   GRASS_REGROWTH_TIME             |   7|
|La probabilité d'apparition de l'herbe              |   GRASS_GROWTH_PROBABILITY        |0.08|




## REGLES

### La grille
Une case contient :\
    - De l'herbe (ou sol vide)\
    - Un seul animal maximum (mouton OU loup, pas deux loups ou deux moutons non plus)\
Une case peut contenir à la fois de l'herbe (ou du sol vide) et un animal.

La grille est fermée, les bords sont infranchissables.\
\On ne considère pas les cases en diagonales dans les fonctions des animaux, ils ne peuvent interagir qu'avec les 4 cases orthogonales les entourant (haut, bas, gauche, droite).

### L'écosystème

Le mouton se déplace soit aléatoirement vers une case libre, mais s'il détecte de l'herbe dans une case adjacente il s'y déplacera au prochain tour.\
Si un mouton est sur une case qui contient de l'herbe, il peut manger celle-ci et gagner de l'énergie.\
Si l'énergie du mouton dépasse un certain seuil, il peut alors se reproduire. Cette opération lui coûte de l'énergie. Le mouton ainsi créé apparaît sur une case adjacente.\
Le mouton meurt si son énergie est inférieure à 0, si son âge dépasse l'âge limite ou s'il est mangé par un loup.\

Le loup a un fonctionnement similaire à celui du mouton, l'herbe étant remplacée par les moutons et qu'il n'a pas de prédateurs. Certains paramètres des loups sont différents de ceux des moutons.\

L'herbe a deux états : présente ou absente (sol vide). Elle dispose d'un paramètres de temps de repousse (comptabilisé en nombre de tours).\
L'herbe peut apparaître aléatoirement sur un sol vide selon une probabilité.\
L'herbe disparaît si elle est mangée par un mouton.\

### Le cycle de simulation

PHASE 1 : AGE\
On incrémente l'âge de tous les animaux

PHASE 2 : Mise à jour de l'herbe\
L'herbe est mise à jour, elle repousse, apparaît aléatoirement ou disparaît si un mouton est sur la même case. 

PHASE 3 : Phase moutons\
Le mouton détecte l'herbe adjacente, se déplace, mange et perd de l'énergie.

PHASE 4 : Phase loups\
Le loup détecte les moutons adjactents, se déplace, mange et perd de l'énergie.

PHASE 5 : Vérification des morts\
On regarde les conditions d'énergies et d'âge.

PHASE 6 : Reproduction\
Si les conditions sont remplies, les animaux peuvent se reproduire.

PHASE 7 : Affichage de l'état actuel\
On affiche la situation obtenue à partir des phases précédentes.

PHASE 8 : Vérifications des conditions d'arrêt\
Si le nombre de tours maximum a été atteint (par défaut, 500), ou s'il n'y a plus d'animaux, on met fin à la simulation.


### Les bonus

Les saisons\
Le nombre de tours est divisé en quatre portions représentant les quatre saisons.\
Cette variation de saison a pour seul effet de modifier la croissance de l'herbe.\
|Saison| Type| Temps de repousse | Probabilité de repousse|
|---|---|:-:|:-:|
|Première saison | hiver| 7|0.08|
|Deuxième saison | printemps| 6 | 0.09|
|Troisième saison | été | 5| 0.08|
|Quatrième saison | automne | 6|0.09|