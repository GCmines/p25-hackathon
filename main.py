from entities import Sheep
from entities2 import Wolves, Grass
from grid import GRID










# DÉROULÉ DU TOUR
    # INCREMENT DE L'AGE DES ANIMAUX




    # MISE A JOUR DE L'HERBE
for x in range(0, GRID_SIZE - 1):                                   # On parcourt les x et y
    for y in range(0, GRID_SIZE - 1):
        Grass.eaten_grass(x, y)                                     # On regarde si l'herbe a été mangée
        Grass.new_grass(x, y)                                       # On regarde si l'herbe peut apparaitre aléatoirement
        Grass.regrowth(x, y)