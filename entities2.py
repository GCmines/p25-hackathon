
from grid import GRID
from entities import Sheep
import random


class Grass:                                                                    # Définition de la classe GRASS (herbe)
    def __init__(self, STATE, TIME, GRASS_REGROWTH_TIME, GRASS_GROWTH_PROBABILITY):
        self.STATE = STATE                                                      # Propriété state (état)
        self.GRASS_REGROWTH_TIME = GRASS_REGROWTH_TIME                          # Propriété qui définit le GRASS regrowth time (temps de repousse)
        self.GRASS_GROWTH_PROBABILITY = GRASS_GROWTH_PROBABILITY                # Propriété qui définit la probabilité d'apparition de l'herbe
        self.TIME = TIME                                                        # Propriété qui gère le temps de temps de repousse 

    def new_grass(self, x, y):                                                        # Fonction d'apparition de l'herbe POUR LES CASES VIDES
        if GRID.GRASS[x][y].STATE == 0:                                             # Si la case ne contient pas d'herbe
            randomnumber = random.randint(1, 100)                                       # On créé un nombre random entre 1 et 100
            if randomnumber <= self.GRASS_GROWTH_PROBABILITY*100:                       # On la compare à notre taux d'apparition spontané
                GRID.GRASS[x][y].STATE = 1                                                  # Si on est inférieur on égal au taux, on fait apparaître l'herbe
                self.TIME = 0                                                               # On réinitialise le temps de repousse de l'herbe 
            else :                                                                      # Sinon
                GRID.GRASS[x][y].STATE == 0                                                 # On laisse la case vide
        else :
            self.TIME = 0                                                           # Si la case contient de l'herbe, on ne fait rien (si ce n'est laissé le temps de repousse à zéro)
    

    def regrowth(self, x, y):                                                         # Fonction de repousse 
        if GRID.GRASS[x][y].STATE == 0:                                             # Si la case ne contient pas d'herbe
            self.TIME = self.TIME + 1                                                   # On incrémente le temps de repousse
            if GRID.GRASS[x][y].TIME == self.GRASS_REGROWTH_TIME:                           # Si on atteint la durée de repousse
                GRID.GRASS[x][y].STATE = 1                                                  # On dit que l'herbe a poussé, son état passe à 1



    def eaten_grass(self, x, y):                                                      # Détection de l'herbe mangée
        if isinstance(GRID.ELT[x][y], Sheep) == True:
            GRID.GRASS[x][y].STATE = 0
            GRID.GRASS[x][y].TIME = -1                                              # On doit mettre -1 puisque cette fonction est effectuée avant new_grass et regrowth