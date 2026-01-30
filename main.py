from entities import Sheep, Wolves, Grass
import random as rd
from grid import GRID
import pyxel 
import time 
GRID_SIZE = 30



def endgame():
    pyxel.quit()



def game(MAX_TURNS=500):
    # DÉROULÉ DU TOUR
    GRID_SIZE = 30
    SHEEP_INITIAL_ENERGY = 20 
    SHEEP_ENERGY_LOSS_PER_TURN= 1
    REPRODUCTION_ENERGY_COST = 20
    SHEEP_REPRODUCTION_THRESHOLD = 50
    SHEEP_ENERGY_FROM_GRASS = 15
    GRASS_REGROWTH_TIME = 7
    GRASS_GROWTH_PROBABILITY = 0.08
    SHEEP_MAX_AGE = 50
    WOLF_MAX_AGE = 40
    NB_SHEEP_INIT = 50
    NB_WOLVES_INIT = 10
    NB_GRASS_INIT = int(0.3*GRID_SIZE**2)
    WOLF_INITIAL_ENERGY = 40
    
    ## initialisation
    grid = GRID()
    def init_sheep_wolves_grass(n_sheep,n_wolves,n_grass,GRID):
        if n_sheep + n_wolves > GRID_SIZE**2:
            return False
        else:
            T = [[(i,j) for j in range (GRID_SIZE)] for i in range(GRID_SIZE)]
            L1 = []
            for ligne in T:
                for elt in ligne:
                    L1.append(elt)
            L2 = rd.sample(L1,n_sheep+n_wolves)
            Ls = rd.sample(L1,n_sheep)
            for i,j in Ls:
                GRID.ELT[i][j] = Sheep((i,j))
            for i,j in L2:
                if (i,j) not in Ls:
                    GRID.ELT[i][j] = Wolves((i,j))
            Lg = rd.sample(L1,n_grass)
            for i,j in L1:
                GRID.ELT[i][j] = Grass(0, 0, GRASS_REGROWTH_TIME, GRASS_GROWTH_PROBABILITY)
            for i,j in Lg:
                GRID.ELT[i][j].STATE = 1 
    
    init_sheep_wolves_grass(NB_SHEEP_INIT,NB_WOLVES_INIT,NB_GRASS_INIT,grid)
    pyxel.init(GRID_SIZE,GRID_SIZE,title = "Ecosystème",fps = 10)
    number_of_animals = 1
    turn_number = 0
    while (turn_number < MAX_TURNS) and (number_of_animals>0):
        turn_number += 1
        tour(grid)
        number_of_animals = 0
        for ligne in grid.ELT:
            for elt in ligne:
                if isinstance(elt, Sheep) or isinstance(elt, Wolves):
                    number_of_animals += 1
        pyxel.run(tour(grid),draw(grid,GRID_SIZE))
    
        
    endgame()


def tour(grid):
    time.sleep(1)
    # PHASE 1 : INCREMENT DE L'AGE DES ANIMAUX
    for ligne in grid.ELT:
        for elt in ligne:
            if isinstance(elt, Sheep) or isinstance(elt, Wolves):
                elt.age()
                
                                    
    # PHASE 2 : MISE A JOUR DE L'HERBE
    for ligne in grid.ELT:
        for elt in ligne:
            elt.eaten_grass()                                     # On regarde si l'herbe a été mangée
            elt.new_grass()                                       # On regarde si l'herbe peut apparaitre aléatoirement
            elt.regrowth()                                        # On fait repousser l'herbe en fonction de son temps de repousse


    # PHASE 3 : MOUTONS

    for k in range(GRID_SIZE):
        for l in range(GRID_SIZE):
            # repérage des moutons dans la grille
            if isinstance(grid.ELT[k][l],Sheep):
                current_sheep = grid.ELT[k][l]
                current_sheep.deplacement(current_sheep,grid)   # déplace et alimente les moutons
                current_sheep.energy(current_sheep)

    # PHASE 4 : LOUPS
    for x in range(0, GRID_SIZE - 1):                                 
        for y in range(0, GRID_SIZE - 1):
            if isinstance(grid.ELT[x][y], Wolves):
                wolf = grid.ELT[x][y]
                wolf.age()
                wolf.mouvement()


    # PHASE 6 : REPRODUCTION
    for ligne in grid.ELT:
        for elt in ligne:
            if isinstance(elt, Sheep) or isinstance(elt, Wolves):
                elt.reproduction()


    # PHASE 8 : VÉRIFICATION DES CONDITIONS D'ARRÊT
    number_of_animals = 0                                                                       # On reset notre compteur d'animaux
    for ligne in grid.ELT:                                                                         # On parcourt les x et y
        for elt in ligne:
            if isinstance(elt, Sheep) or isinstance(elt, Wolves):         # On regarde s'il y a des animaux sur notre grille
                number_of_animals += 1
    if number_of_animals == 0:                                                                  # S'il n'y a pas d'animaux, c'est la fin de la simulation
        endgame()


## affichage graphique
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
        
game(500)