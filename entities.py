import random as rd 
GRID_SIZE = 30
SHEEP_INITIAL_ENERGY = 20 
rd.randint(1,GRID_SIZE),rd.randint(1,GRID_SIZE)
class Sheep:
    def __init__(self,POSITION):
        self.POSITION = (POSITION)
        self.AGE = 0
        self.ENERGY = SHEEP_INITIAL_ENERGY
    
    def deplacement(self,GRID):
        i,j = self.POSITION
        GRID.SHEEP[i][j] = 0
        if GRID.GRASS[i][j+1].STATE == 1 and GRID.SHEEP[i][j+1] == 0:
            self.POSITION = (i,j+1)
            self.eat()
        elif GRID.GRASS[i][j-1].STATE == 1 and GRID.SHEEP[i][j+1] == :
            self.POSITION = (i, j-1)
            self.eat()
        elif GRID.GRASS[i-1][j].STATE == 1:
            self.POSITION = (i-1,j)
            self.eat()
        elif GRID.GRASS[i+1][j].STATE == 1:
            self.POSITION = (i+1,j)
            self.eat()
        else: 
            x = rd.randint(0,1)
            self.POSITION = (i+((rd.randint(0,1))*2-1)*(x-1),j+((rd.randint(0,1))*2-1)*x)
    
    def eat(self):
