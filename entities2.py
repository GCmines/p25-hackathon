
from grid import GRID
from entities import Sheep
import random




class Wolves:
    def __init__(self, position):
        self.position = position
        self.energy = WOLF_INITIAL_ENERGY
        self.age = 0

    def eat(self, GRID):
        x, y = self.position
        if x != 0 and isinstance(GRID.ELT[x-1][y], Sheep) :
            return (True, (x-1,y))
        if x != GRID_SIZE - 1 and isinstance(GRID.ELT[x+1][y], Sheep):
            return (True, (x+1,y))
        if y != 0 and isinstance(GRID.ELT[x][y-1], Sheep):
            return (True, (x,y-1))
        if y != GRID_SIZE - 1 and isinstance(GRID.ELT[x][y+1], Sheep):
            return (True, (x,y+1))
        return (False, (x,y))
        

    def death(self, GRID):
        i,j = self.position
        if self.energy <= 0 or self.age > WOLF_MAX_AGE:
            GRID.ELT[i][j] == 0

    def reproduction(self,GRID):
        if self.energy>SHEEP_REPRODUCTION_THRESHOLD:
            i,j = self.position
            self.energy = self.energy - REPRODUCTION_ENERGY_COST
            if (i+1<GRID_SIZE) and (GRID.ELT[i+1][j]==0):
                GRID.ELT[i+1][j] = Wolves((i+1,j))
            elif (i-1>=0) and (GRID.ELT[i-1][j]==0):
                GRID.ELT[i-1][j] = Wolves((i-1,j))
            elif (j+1<GRID_SIZE) and (GRID.ELT[i][j+1]==0):            
                GRID.ELT[i][j+1] = Wolves((i,j+1))
            elif (j-1>0) and (GRID.ELT[i][j-1]==0):            
                GRID.ELT[i][j-1] = Wolves((i,j-1))

    def age(self):
        if (self.age<AGE_LIMITE) and (self.energy >0):
            self.age +=1
        else :
            i,j = self.position
            GRID.ELT[i][j] = 0

    def movement(self, GRID):
        if eat(self)[0] : 
            self.position = eat(self)[1]
        else :
            i,j = self.position
            if j<GRID_SIZE-1 and GRID.GRASS[i][j+1].STATE == 1 and GRID.ELT[i][j+1] == 0:
                self.position = (i,j+1)
                self.eat()
            elif j>0 and GRID.GRASS[i][j-1].STATE == 1 and GRID.ELT[i][j-1] == 0:
                self.position = (i, j-1)
                self.eat()
            elif i>0 and GRID.GRASS[i-1][j].STATE == 1 and GRID.ELT[i][j+1] == 0:
                self.position = (i-1,j)
                self.eat()
            elif i<GRID_SIZE-1 and GRID.GRASS[i+1][j].STATE == 1 and GRID.ELT[i][j+1] == 0:
                self.position = (i+1,j)
                self.eat()
            else: 
                positions = []
                if j<GRID_SIZE-1 and GRID.ELT[i][j+1] == 0 :
                    positions.append((i,j+1))
                elif j>0 and GRID.ELT[i][j+1] == 0 :
                    positions.append((i,j-1))
                elif i>0 and GRID.ELT[i][j+1] == 0 :
                    positions.append((i-1,j))
                elif i<GRID_SIZE-1 and GRID.ELT[i][j+1] == 0 :
                    positions.append((i-1,j))
                if positions != []:
                    self.position = rd.choice(positions)
            sheep = GRID.ELT[i,j]
            GRID.ELT[i,j] = 0
            GRID.ELT[self.position[0]][self.position[1]]
            



class Grass:                                                                    # Définition de la classe GRASS (herbe)
    def __init__(self, STATE, TIME, GRASS_REGROWTH_TIME, GRASS_GROWTH_PROBABILITY):
        self.STATE = STATE                                                      # Propriété state (état)
        self.GRASS_REGROWTH_TIME = GRASS_REGROWTH_TIME                          # Propriété qui définit le GRASS regrowth time (temps de repousse)
        self.GRASS_GROWTH_PROBABILITY = GRASS_GROWTH_PROBABILITY                # Propriété qui définit la probabilité d'apparition de l'herbe
        self.TIME = TIME                                                        # Propriété qui gère le temps de temps de repousse 

    def new_grass(self, x, y):                                                        # Fonction d'apparition de l'herbe POUR LES CASES VIDES
        if GRID.GRASS[x][y].STATE == 0:                                             # Si la case ne contient pas d'herbe
            if random.random(0, 1) <= self.GRASS_GROWTH_PROBABILITY:                       # On la compare à notre taux d'apparition spontané
                GRID.GRASS[x][y].STATE = 1                                                  # Si on est inférieur on égal au taux, on fait apparaître l'herbe
                self.TIME = 0                                                               # On réinitialise le temps de repousse de l'herbe

    def regrowth(self, x, y):                                                         # Fonction de repousse 
        if GRID.GRASS[x][y].STATE == 0:                                             # Si la case ne contient pas d'herbe
            self.TIME = self.TIME + 1                                                   # On incrémente le temps de repousse
            if GRID.GRASS[x][y].TIME == self.GRASS_REGROWTH_TIME:                           # Si on atteint la durée de repousse
                GRID.GRASS[x][y].STATE = 1                                                  # On dit que l'herbe a poussé, son état passe à 1

    def eaten_grass(self, x, y):                                                      # Détection de l'herbe mangée
        if isinstance(GRID.ELT[x][y], Sheep) == True:
            GRID.GRASS[x][y].STATE = 0
            GRID.GRASS[x][y].TIME = -1                                              # On doit mettre -1 puisque cette fonction est effectuée avant new_grass et regrowth


