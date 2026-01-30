import numpy as np

## Modélisation de la grille
GRID_SIZE = 30
class GRID:
    def __init__(self):
        self.SIZE = GRID_SIZE
        self.GRASS = np.zeros(shape =(GRID_SIZE,GRID_SIZE))
        self.ELT = np.zeros(shape = (GRID_SIZE,GRID_SIZE))


    


    