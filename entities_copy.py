import random as rd 
from grid_copy import Grid



# On initialise certaines variables, voir le README pour avoir les explications
GRID_SIZE = 30
SHEEP_INITIAL_ENERGY = 20 
SHEEP_ENERGY_LOSS_PER_TURN= 1
REPRODUCTION_ENERGY_COST = 20
SHEEP_REPRODUCTION_THRESHOLD = 50
SHEEP_ENERGY_FROM_GRASS = 15
SHEEP_MAX_AGE = 50
WOLF_MAX_AGE = 40
WOLF_INITIAL_ENERGY = 40


class Sheep:                                                                                # On définit la classe Sheep (mouton)
    def __init__(self,POSITION):                                                            # On initialise les paramètres initiaux des moutons
        self.POSITION = (POSITION)
        self.AGE = 0
        self.ENERGY = SHEEP_INITIAL_ENERGY
    
    def deplacement(self,GRID):                                                             # On créé la fonction de déplacement du mouton
        i,j = self.POSITION
        if j<GRID_SIZE-1 and GRID.GRASS[i][j+1].STATE == 1 and GRID.ELT[i][j+1] == 0:
            self.POSITION = (i,j+1)
            self.eat()
        elif j>0 and GRID.GRASS[i][j-1].STATE == 1 and GRID.ELT[i][j-1] == 0:
            self.POSITION = (i, j-1)
            self.eat()
        elif i>0 and GRID.GRASS[i-1][j].STATE == 1 and GRID.ELT[i][j+1] == 0:
            self.POSITION = (i-1,j)
            self.eat()
        elif i<GRID_SIZE-1 and GRID.GRASS[i+1][j].STATE == 1 and GRID.ELT[i][j+1] == 0:
            self.POSITION = (i+1,j)
            self.eat()
        else: 
            position = []
            if j<GRID_SIZE-1 and GRID.ELT[i][j+1] == 0 :
                position.append((i,j+1))
            elif j>0 and GRID.ELT[i][j+1] == 0 :
                position.append((i,j-1))
            elif i>0 and GRID.ELT[i][j+1] == 0 :
                position.append((i-1,j))
            elif i<GRID_SIZE-1 and GRID.ELT[i][j+1] == 0 :
                position.append((i-1,j))
            if position != []:
                self.POSITION = rd.choice(position)
        sheep = GRID.ELT[i,j]
        GRID.ELT[i,j] = 0
        GRID.ELT[self.POSITION[0]][self.POSITION[1]] = sheep
        
    def eat(self):                                                                          # On créé la fonction qui permet au mouton de gagner de l'énergie en mangeant de l'herbe
        self.ENERGY= self.ENERGY +SHEEP_ENERGY_FROM_GRASS
        
    def energy(self):                                                                       # On créé la fonction qui fait perdre de l'énergie au mouton à chaque tour
        self.ENERGY = self.ENERGY -SHEEP_ENERGY_LOSS_PER_TURN

    def age(self):                                                                          # On créé la fonction qui gère l'âge du mouton et qui vérifie s'il doit mourir
        if (self.AGE<SHEEP_MAX_AGE) and (self.ENERGY >0):
            self.AGE +=1
        else :
            i,j = self.POSITION
            GRID.ELT[i][j] = 0
    
    def reproduction(self,GRID):                                                            # On créé la fonction de reproduction du mouton
        if self.ENERGY>SHEEP_REPRODUCTION_THRESHOLD:
            i,j = self.POSITION
            self.ENERGY = self.ENERGY - REPRODUCTION_ENERGY_COST
            if (i+1<GRID_SIZE) and (GRID.ELT[i+1][j]==0):
                GRID.ELT[i+1][j] = Sheep((i+1,j))
            elif (i-1>=0) and (GRID.ELT[i-1][j]==0):
                GRID.ELT[i-1][j] = Sheep((i-1,j))
            elif (j+1<GRID_SIZE) and (GRID.ELT[i][j+1]==0):            
                GRID.ELT[i][j+1] = Sheep((i,j+1))
            elif (j-1>0) and (GRID.ELT[i][j-1]==0):            
                GRID.ELT[i][j-1] = Sheep((i,j-1))
            
    


class Wolves:                                                                               # On créé la classe Wolves (Loups)
    def __init__(self, position):                                                           # On initialise les paramètres initiaux du loup
        self.position = position
        self.energy = WOLF_INITIAL_ENERGY
        self.age = 0

    def eat(self, GRID):                                                                    # On créé la fonction qui détecte les moutons à manger
        x, y = self.position
        if x != 0 and isinstance(GRID.ELT[x-1][y], Sheep) :
            GRID.ELT[x][y] = 0
            return (True, (x-1,y))
        if x != GRID_SIZE - 1 and isinstance(GRID.ELT[x+1][y], Sheep):
            GRID.ELT[x][y] = 0
            return (True, (x+1,y))
        if y != 0 and isinstance(GRID.ELT[x][y-1], Sheep):
            GRID.ELT[x][y] = 0
            return (True, (x,y-1))
        if y != GRID_SIZE - 1 and isinstance(GRID.ELT[x][y+1], Sheep):
            GRID.ELT[x][y] = 0
            return (True, (x,y+1))
        return (False, (x,y))

    def reproduction(self,GRID):                                                            # On créé la fonction de reproduction du loup
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

    def age(self, GRID):                                                                    # On créé la fonction qui gère l'âge du loup et qui vérifie s'il doit mourir
        if (self.age<WOLF_MAX_AGE) and (self.energy >0):
            self.age +=1
        else :
            i,j = self.position
            GRID.ELT[i][j] = 0

    def movement(self, GRID):                                                               # On créé la fonction
        if eat(self)[0] : 
            self.position = eat(self)[1]
            x, y = self.position 
            GRID.ELT[x][y] = self
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
            GRID.ELT[i,j] = 0
            GRID.ELT[self.position[0]][self.position[1]] = self
            



class Grass:                                                                        # Définition de la classe GRASS (herbe)
    def __init__(self, STATE, TIME, GRASS_REGROWTH_TIME, GRASS_GROWTH_PROBABILITY):
        self.STATE = STATE                                                          # Propriété state (état)
        self.GRASS_REGROWTH_TIME = GRASS_REGROWTH_TIME                              # Propriété qui définit le GRASS regrowth time (temps de repousse)
        self.GRASS_GROWTH_PROBABILITY = GRASS_GROWTH_PROBABILITY                    # Propriété qui définit la probabilité d'apparition de l'herbe
        self.TIME = TIME                                                            # Propriété qui gère le temps de temps de repousse 

    def new_grass(self):                                                            # Fonction d'apparition de l'herbe POUR LES CASES VIDES
        if self.STATE == 0:                                                             # Si la case ne contient pas d'herbe
            if rd.random() <= self.GRASS_GROWTH_PROBABILITY:                            # On la compare à notre taux d'apparition spontané
                self.STATE = 1                                                              # Si on est inférieur on égal au taux, on fait apparaître l'herbe
                self.TIME = 0                                                               # On réinitialise le temps de repousse de l'herbe

    def regrowth(self):                                                             # Fonction de repousse 
        if self.STATE == 0:                                                             # Si la case ne contient pas d'herbe
            self.TIME = self.TIME + 1                                                   # On incrémente le temps de repousse
            if self.TIME == self.GRASS_REGROWTH_TIME:                                       # Si on atteint la durée de repousse
                self.STATE = 1                                                              # On dit que l'herbe a poussé, son état passe à 1

    def eaten_grass(self):                                                          # Détection de l'herbe mangée
        if isinstance(self, Sheep) == True:
            self.STATE = 0
            self.TIME = -1                                                              # On doit mettre -1 puisque cette fonction est effectuée avant new_grass et regrowth


