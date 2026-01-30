import numpy as np

## Modélisation de la grille
GRID_SIZE = 30
class GRID:
    def __init__(self):
        self.SIZE = GRID_SIZE
        self.GRASS = [[0 for i in range(GRID_SIZE)]for j in range(GRID_SIZE)]
        self.ELT = [[0 for i in range(GRID_SIZE)]for j in range(GRID_SIZE)]

    


    