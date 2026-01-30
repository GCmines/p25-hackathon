import numpy as np

## Modélisation de la grille
GRID_SIZE = 30
class GRID:
    def __init__(self):
        self.SIZE = GRID_SIZE                                                               # Le paramètre de la taille de la grille est initialisé
        self.GRASS = [[0 for i in range(GRID_SIZE)]for j in range(GRID_SIZE)]               # On créé une grille d'herbe/de sol
        self.ELT = [[0 for i in range(GRID_SIZE)]for j in range(GRID_SIZE)]                 # On créé une grille pour les animaux

    


    