from dataclasses import dataclass
import random as rd


@dataclass
class Animal:
    position: tuple[int]
    age: int
    energy: int

    def eat(self, energy_gain):
        self.energy = self.energy + energy_gain
    


@dataclass
class Sheep(Animal):
    
    def deplacement(self, grille, gsize, gain):
        i, j = self.position
        if j<gsize-1 and grille.grass[i][j+1].state == 1 and grille.animals[i][j+1] == 0:
            self.position = (i,j+1)
            self.eat(gain)
        elif j>0 and grille.grass[i][j-1].state == 1 and grille.animals[i][j-1] == 0:
            self.position = (i, j-1)
            self.eat(gain)
        elif i>0 and grille.grass[i-1][j].state == 1 and grille.animals[i][j+1] == 0:
            self.position = (i-1,j)
            self.eat(gain)
        elif i<gsize-1 and grille.grass[i+1][j].state == 1 and grille.animals[i][j+1] == 0:
            self.position = (i+1,j)
            self.eat(gain)
        else: 
            nextposition = []
            if j<gsize-1 and grille.animals[i][j+1] == 0 :
                nextposition.append((i,j+1))
            elif j>0 and grille.animals[i][j+1] == 0 :
                nextposition.append((i,j-1))
            elif i>0 and grille.animals[i][j+1] == 0 :
                nextposition.append((i-1,j))
            elif i<gsize-1 and grille.animals[i][j+1] == 0 :
                nextposition.append((i-1,j))
            if nextposition != []:
                self.position = rd.choice(nextposition)



@dataclass
class Wolf(Animal):
    def



@dataclass
class grass:                                        # Définition de la classe grass (herbe)
    state: int                                          # Propriété state (état). 0 pour un sol vide, 1 pour de l'herbe
    time: int                                           # Propriété time (temps), donne le temps de repousse

    def new_grass(self, proba):                         # Fonction d'apparition de l'herbe aléatoirement sur un sol vide
        if self.state == 0:                                 # Si la case ne contient pas d'herbe
            if rd.random(0, 1) <= proba:                        # On la compare à notre taux d'apparition spontané
                self.state = 1                                  # Si on remplit la condition, on fait apparaître l'herbe
                self.time = 0                                   # On réinitialise le temps de repousse de l'herbe
    
    def regrowth(self, time):                           # Fonction de repousse
        if self.state == 0:                                 # Si la case ne contient pas d'herbe
            self.time += 1                                      # On incrémente le temps de repousse
            if self.time == time:                                   # Si on atteint la durée de repousse
                self.state = 1                                      # On fait apparaître de l'herbe
                self.time = 0                                       # On réinitialise le temps de repousse
    
    def eaten_grass(self):                              # Fonction de détection de l'herbe mangée
        if isinstance(self, Sheep) == True:                 # Si un mouton est sur la case (c'est qu'il a mangé l'herbe)
            self.state = 0                                      # On enlève l'herbe
            self.time = -1                                      # On passe son temps de repousse à -1 (cette fonction est effectuée avant new_grass et regrowth)