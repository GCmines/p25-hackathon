import numpy as np

## Modélisation de la grille
GRID_SIZE = 30
class GRID:
    def __init__(self):
        self.SIZE = GRID_SIZE
        self.GRASS = np.array('N',shape =(GRID_SIZE,GRID_SIZE))
        self.SHEEP = np.array('N',shape = (GRID_SIZE,GRID_SIZE))
        self.WOLF = np.array('N',shape = (GRID_SIZE,GRID_SIZE))

    


    