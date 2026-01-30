import numpy as np
from dataclasses import dataclass
from entities2 import Grass, Animal


'''
## Modélisation de la grille
GRID_SIZE = 30
class GRID:
    def __init__(self):
        self.SIZE = GRID_SIZE                                                               # Le paramètre de la taille de la grille est initialisé
        self.GRASS = [[0 for i in range(GRID_SIZE)]for j in range(GRID_SIZE)]               # On créé une grille d'herbe/de sol
        self.ELT = [[0 for i in range(GRID_SIZE)]for j in range(GRID_SIZE)]                 # On créé une grille pour les animaux
'''


@dataclass
class Grid: 
    size: int
    grass: list[list[Grass]]
    animals: list[list[Animal]]
