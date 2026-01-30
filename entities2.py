class Wolves:
    def __init__(self, position):
        self.position = position
        self.energy = WOLF_INITIAL_ENERGY
        self.age = 0
        self.ALIVE = True

    def eat(self):
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
        

    def death(self):
        if self.energy <= 0 or self.age > WOLF_MAX_AGE:
            self.ALIVE = False



    def reproduction(self):.
        if self.energy > WOLF_REPRODUCTION_THRESHOLD:
            self.energy -= REPRODUCTION_ENERGY_COST
            return True


    def movement(self):
        if eat(self)[0] : 
            self.position = eat(self)[1]
        else :
            
