from entities import Sheep
from entities2 import Wolves, Grass
from grid import GRID
import pyxel 
GRID_SIZE = 30



def endgame(): 


def initgame():


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

    for k in range(GRID_SIZE):
        for l in range(GRID_SIZE):
            # repérage des moutons dans la grille
            if isinstance(grid.ELT[k][l],Sheep):
                current_sheep = grid.ELT[k][l]
                current_sheep.deplacement(current_sheep,grid)   # déplace et alimente les moutons
                current_sheep.energy(current_sheep)

    # PHASE 4 : LOUPS
    # PHASE 5 : Vérification des morts???
    # PHASE 6 : REPRODUCTION
    # PHASE 7 : AFFICHAGE DE L'ÉTAT OBTENU
    
    # faire le lien entre classe et affichage
    pyxel.init(GRID_SIZE,GRID_SIZE,title = "Ecosystème")
    def draw(grille,taille):
        for a in range(taille):
            for b in range(taille):
                if isinstance(grille.ELT[k][l],Sheep):
                    pyxel.pset(a,b,7)
                elif isinstance(grille.ELT[k][l],Wolves):
                    pyxel.pset(a,b,13)
                elif (grille.GRASS[a][b].STATE ==1):
                    pyxel.pset(a,b,11) 
                else :
                    pyxel.pset(a,b,9)
    pyxel.run(draw(grid,GRID_SIZE))


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
