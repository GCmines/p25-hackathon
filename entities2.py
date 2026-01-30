from dataclasses import dataclass
import random as rd


@dataclass
class Animal:                                                           # Classe mère Animale permettant de réunir les fonctions communes aux loups et aux moutons (à quelques détails près) 
    position: tuple[int]                                                    # Position sur la grille de l'animal
    age: int                                                                # Age de l'animal (en nombre de tours)
    energy: int                                                             # Energie de l'animal

    def eat(self, energy_gain):                                             # Fonction donnant l'énergie à l'animal quand il mange
        self.energy = self.energy + energy_gain
    
    def energy_natural_loss(self, turn_cost):                               # Fonction faisait perdre de l'énergie naturellement à l'animal pendant un tour
        self.energy = self.energy - turn_cost

    def reproduction(self, grille, gsize, threshold, cost, classe):         # Fonction de reproduction de l'animal
        if self.energy > threshold:
            i, j = self.position
            self.energy = self.energy - cost
            if (i+1 < gsize) and (grille.animals[i+1][j]==0):
                grille.animals[i+1][j] = classe((i+1, j), 0, 0)
            if (i-1 > 0) and (grille.animals[i-1][j]==0):
                grille.animals[i-1][j] = classe((i-1, j), 0, 0)
            if (j+1 < gsize) and (grille.animals[i][j+1]==0):
                grille.animals[i][j+1] = classe((i, j+1), 0, 0)
            if (j-1 > 0) and (grille.animals[i][j-1]==0):
                grille.animals[i][j-1] = classe((i, j-1), 0, 0)

    def gettin_old(self, max_age):                               # Fonction faisant grandir l'animal
        if (self.age < max_age) and (self.energy > 0):
            self.age += 1
    
    def death_verification(self, max_age, grille):
        if (self.age == max_age) and (self.energy == 0):
            i, j = self.position
            grille.animals[i][j] = 0

@dataclass
class Sheep(Animal):                                                    # Classe du mouton

    def deplacement(self, grille, gsize, gain):                             # Fonction gérant la "vision" des alentours du mouton et ses déplacements
        i, j = self.position
        if j<gsize-1 and grille.grass[i][j+1].state == 1 and grille.animals[i][j+1] == 0:
            self.position = (i,j+1)
            a, b = i, j+1
            self.eat(gain)
        elif j>0 and grille.grass[i][j-1].state == 1 and grille.animals[i][j-1] == 0:
            self.position = (i, j-1)
            a, b = i, j-1
            self.eat(gain)
        elif i>0 and grille.grass[i-1][j].state == 1 and grille.animals[i-1][j] == 0:
            self.position = (i-1,j)
            a, b = i-1, j
            self.eat(gain)
        elif i<gsize-1 and grille.grass[i+1][j].state == 1 and grille.animals[i+1][j] == 0:
            self.position = (i+1,j)
            a, b = i+1, j
            self.eat(gain)
        else: 
            nextposition = []
            if j<gsize-1 and grille.animals[i][j+1] == 0:
                nextposition.append((i,j+1))
            elif j>0 and grille.animals[i][j-1] == 0:
                nextposition.append((i,j-1))
            elif i>0 and grille.animals[i-1][j] == 0:
                nextposition.append((i-1,j))
            elif i<gsize-1 and grille.animals[i+1][j] == 0:
                nextposition.append((i+1,j))
            if nextposition != []:
                self.position = rd.choice(nextposition)
                (a, b) = self.position
            else:
                a, b = i, j

        grille.animals[i][j] = 0
        grille.animals[a][b] = self

@dataclass
class Wolf(Animal):                                                     # Classe du loup
    
    def deplacement(self, grille, gsize, gain):                             # Fonction gérant la "vision" des alentours du loup et ses déplacements
        i, j = self.position
        if j<gsize-1 and isinstance(grille.animals[i][j+1], Sheep):
            self.position = (i,j+1)
            a, b = i, j+1
            self.eat(gain)
        elif j>0 and isinstance(grille.animals[i][j-1], Sheep):
            self.position = (i, j-1)
            a, b = i, j-1
            self.eat(gain)
        elif i>0 and isinstance(grille.animals[i-1][j], Sheep):
            self.position = (i-1,j)
            a, b = i-1, j
            self.eat(gain)
        elif i<gsize-1 and isinstance(grille.animals[i+1][j], Sheep):
            self.position = (i+1,j)
            a, b = i+1, j
            self.eat(gain)
        else: 
            nextposition = []
            if j<gsize-1 and grille.animals[i][j+1] == 0 :
                nextposition.append((i,j+1))
            elif j>0 and grille.animals[i][j-1] == 0 :
                nextposition.append((i,j-1))
            elif i>0 and grille.animals[i-1][j] == 0 :
                nextposition.append((i-1,j))
            elif i<gsize-1 and grille.animals[i+1][j] == 0 :
                nextposition.append((i+1,j))
            if nextposition != []:
                self.position = rd.choice(nextposition)
                (a, b) = self.position
            else: 
                a, b = i, j
        
        grille.animals[i][j] = 0
        grille.animals[a][b] = self


@dataclass
class Grass:                                                            # Classe de l'herbe
    state: int                                                              # Propriété state (état). 0 pour un sol vide, 1 pour de l'herbe
    time: int                                                               # Propriété time (temps), donne le temps de repousse

    def new_grass(self, proba):                                             # Fonction d'apparition de l'herbe aléatoirement sur un sol vide
        if self.state == 0:                                 # Si la case ne contient pas d'herbe
            if rd.random() <= proba:                        # On la compare à notre taux d'apparition spontané
                self.state = 1                                  # Si on remplit la condition, on fait apparaître l'herbe
                self.time = 0                                   # On réinitialise le temps de repousse de l'herbe
    
    def regrowth(self, time):                                               # Fonction de repousse
        if self.state == 0:                                 # Si la case ne contient pas d'herbe
            self.time += 1                                      # On incrémente le temps de repousse
            if self.time == time:                                   # Si on atteint la durée de repousse
                self.state = 1                                      # On fait apparaître de l'herbe
                self.time = 0                                       # On réinitialise le temps de repousse
    
    def eaten_grass(self):                                                  # Fonction de détection de l'herbe mangée
        if isinstance(self, Sheep) == True:                 # Si un mouton est sur la case (c'est qu'il a mangé l'herbe)
            self.state = 0                                      # On enlève l'herbe
            self.time = -1                                      # On passe son temps de repousse à -1 (cette fonction est effectuée avant new_grass et regrowth)