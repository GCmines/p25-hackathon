from entities import Sheep
from entities2 import Wolves, Grass
from grid import GRID
GRID_SIZE = 30









# DÉROULÉ DU TOUR
# PHASE 1 : INCREMENT DE L'AGE DES ANIMAUX
for ligne in GRID.ELT:
    for elt in ligne:
        if isinstance(elt, Sheep) or isinstance(elt, Wolves):
            elt.age()
# PHASE 2 : MISE A JOUR DE L'HERBE
for x in range(0, GRID_SIZE - 1):                                   # On parcourt les x et y
    for y in range(0, GRID_SIZE - 1):
        Grass.eaten_grass(x, y)                                     # On regarde si l'herbe a été mangée
        Grass.new_grass(x, y)                                       # On regarde si l'herbe peut apparaitre aléatoirement
        Grass.regrowth(x, y)                                        # On fait repousser l'herbe en fonction de son temps de repousse

# PHASE 3 : MOUTONS
# PHASE 4 : LOUPS
# PHASE 5 : Vérification des morts???
# PHASE 6 : REPRODUCTION
# PHASE 7 : AFFICHAGE DE L'ÉTAT OBTENU


# PHASE 8 : VÉRIFICATION DES CONDITIONS D'ARRÊT

