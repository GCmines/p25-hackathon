from entities import Sheep
from entities2 import Wolves, Grass
from grid import GRID




def endgame():


def initgame():
    


def tour(MAX_TURNS=500):
    turn_number = 0
    # DÉROULÉ DU TOUR
    turn_number += 1
    # PHASE 1 : INCREMENT DE L'AGE DES ANIMAUX




    # PHASE 2 : MISE A JOUR DE L'HERBE
    for x in GRID_SIZE:                                   # On parcourt les x et y
        for y in GRID_SIZE:
            Grass.eaten_grass(x, y)                                     # On regarde si l'herbe a été mangée
            Grass.new_grass(x, y)                                       # On regarde si l'herbe peut apparaitre aléatoirement
            Grass.regrowth(x, y)                                        # On fait repousser l'herbe en fonction de son temps de repousse

    # PHASE 3 : MOUTONS
    # PHASE 4 : LOUPS
    # PHASE 5 : Vérification des morts???
    # PHASE 6 : REPRODUCTION
    # PHASE 7 : AFFICHAGE DE L'ÉTAT OBTENU


    # PHASE 8 : VÉRIFICATION DES CONDITIONS D'ARRÊT
    if turn_number == MAX_TURNS:                                    # On arrête le jeu si on a atteint le nombre de tours maximum
        endgame()
    number_of_animals = 0
    for x in range(0, GRID_SIZE - 1):                                   # On parcourt les x et y
        for y in range(0, GRID_SIZE - 1):
            if isinstance(GRID.ELT[x][y], Sheep) or isinstance(GRID.ELT[x][y], Wolves):
                number_of_animals += 1
    if number_of_animals == 0:
        endgame()
