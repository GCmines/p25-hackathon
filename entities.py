import random as rd 
GRID_SIZE = 30
SHEEP_INITIAL_ENERGY = 20 
rd.randint(1,GRID_SIZE),rd.randint(1,GRID_SIZE)
x = rd.randint(0,1)
self.POSITION = (i+((rd.randint(0,1))*2-1)*(x-1),j+((rd.randint(0,1))*2-1)*x)
class Sheep:
    def __init__(self,POSITION):
        self.POSITION = (POSITION)
        self.AGE = 0
        self.ENERGY = SHEEP_INITIAL_ENERGY
        self.ALIVE = True
    
    def deplacement(self,GRID):
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
            elif j>0 and GRID.ELT[i][j+1] ==0 :
                position.append((i,j-1))
            elif i>0 and GRID.ELT[i][j+1] == 0 :
                position.append((i-1,j))
            elif i<GRID_SIZE-1 and GRID.ELT[i][j+1] == 0 :
                position.append((i-1,j))
            if position != []:
                self.POSITION = rd.choice(position)
        sheep = GRID.ELT[i,j]
        GRID.ELT[i,j] = 0
        GRID.ELT[self.POSITION[0]][self.POSITION[1]]
        
    def eat(self):
        self.ENERGY= self.ENERGY +SHEEP_ENERGY_FROM_GRASS
        

    def age(self):
        if (self.AGE<AGE_LIMITE) and (self.ALIVE):
            self.AGE +=1
            self.ENERGY = self.ENERGY -SHEEP_ENERGY_LOSS_PER_TURN
        elif self.AGE>=AGE_LIMITE :
            i,j = self.POSITION
            GRID.ELT[i][j] = 0
    
    def reproduction(self,GRID):
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
            
    

