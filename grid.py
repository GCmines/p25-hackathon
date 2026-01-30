import numpy as np

## Modélisation de la grille
GRID_SIZE = 30
class GRID:
    def __init__(self):
        self.SIZE = GRID_SIZE
        self.GRASS = np.empty(shape =(GRID_SIZE,GRID_SIZE))
        self.ELT = np.empty(shape = (GRID_SIZE,GRID_SIZE))


    


    