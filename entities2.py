from grid import Grid
import random


class Grass:                                                                    # Définition de la classe Grass (herbe)
    def __init__(self, STATE, TIME, GRASS_REGROWTH_TIME, GRASS_GROWTH_PROBABILITY):
        self.STATE = STATE                                                      # Propriété state (état)
        self.GRASS_REGROWTH_TIME = GRASS_REGROWTH_TIME                          # Propriété qui définit le grass regrowth time (temps de repousse)
        self.GRASS_GROWTH_PROBABILITY = GRASS_GROWTH_PROBABILITY                # Propriété qui définit la probabilité d'apparition de l'herbe
        self.TIME = TIME                                                        # Propriété qui gère le temps de temps de repousse 

    def new_grass(self):                                                        # Fonction d'apparition de l'herbe POUR LES CASES VIDES
        if Grid.grass[x][y].STATE == 0:                                             # Si la case ne contient pas d'herbe
            randomnumber = random.randint(1, 100)                                       # On créé un nombre random entre 1 et 100
            if randomnumber <= self.GRASS_GROWTH_PROBABILITY*100:                       # On la compare à notre taux d'apparition spontané
                Grid.grass[x][y].STATE = 1                                                  # Si on est inférieur on égal au taux, on fait apparaître l'herbe
                self.TIME = 0                                                               # On réinitialise le temps de repousse de l'herbe 
            else :                                                                      # Sinon
                Grid.grass[x][y].STATE == 0                                                 # On laisse la case vide
        else :
            self.TIME = 0                                                           # Si la case contient de l'herbe, on ne fait rien (si ce n'est laissé le temps de repousse à zéro)
    

    def eaten_grass(self):                                                      # Détection de l'herbe mangée
        
    
    def regrowth(self):                                                         # Fonction de repousse 
        if Grid.grass[x][y].STATE == 0:                                             # Si la case ne contient pas d'herbe
            self.TIME = self.TIME + 1                                                   # On incrémente le temps de repousse
            if Grid.grass[x][y].TIME == self.GRASS_REGROWTH_TIME:                           # Si on atteint la durée de repousse
                Grid.grass[x][y].STATE = 1                                                  # On dit que l'herbe a poussé, son état passe à 1
                
            else 
            
