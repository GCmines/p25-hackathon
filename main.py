from entities import Sheep
from entities2 import Wolves, Grass
from grid import GRID
GRID_SIZE = 30



def endgame():


def initgame():
     # DÉROULÉ DU TOUR
    turn_number += 1
    turn_number = 0



def tour(MAX_TURNS=500):
   

    # PHASE 1 : INCREMENT DE L'AGE DES ANIMAUX
    for ligne in GRID.ELT:
        for elt in ligne:
            if isinstance(elt, Sheep) or isinstance(elt, Wolves):
                elt.age()
                
                                    
    # PHASE 2 : MISE A JOUR DE L'HERBE
    for ligne in GRID.ELT:
        for elt in ligne:
            elt.eaten_grass()                                     # On regarde si l'herbe a été mangée
            elt.new_grass()                                       # On regarde si l'herbe peut apparaitre aléatoirement
            elt.regrowth()                                        # On fait repousser l'herbe en fonction de son temps de repousse


    # PHASE 3 : MOUTONS


    # PHASE 4 : LOUPS


    # PHASE 5 : Vérification des morts???

    # PHASE 6 : REPRODUCTION
    
    # PHASE 7 : AFFICHAGE DE L'ÉTAT OBTENU


    # PHASE 8 : VÉRIFICATION DES CONDITIONS D'ARRÊT
    if turn_number == MAX_TURNS:                                    # On arrête le jeu si on a atteint le nombre de tours maximum
        endgame()
    number_of_animals = 0
    for x in GRID_SIZE:                                   # On parcourt les x et y
        for y in GRID_SIZE:
            if isinstance(GRID.ELT[x][y], Sheep) or isinstance(GRID.ELT[x][y], Wolves):
                number_of_animals += 1
    if number_of_animals == 0:
        endgame()
