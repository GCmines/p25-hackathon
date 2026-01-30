from dataclasses import dataclass
import random as rd


@dataclass
class Animal:
    position: tuple[int]
    age: int
    energy: int

    def eat(self, )
        



@dataclass
class Sheep(Animal):
    def



@dataclass
class Wolf(Animal):
    def



@dataclass
class Grass:
    state: int
    time: int

    def new_grass(self, proba):
        if self.state == 0:
            if rd.random(0, 1) <= proba:
                self.state = 1
                self.time = 0
    
    def regrowth(self, time):
        if self.state == 0:
            self.time += 1
            if self.time == time
                self.state = 1
    
    def eaten_grass(self):
        if isinstance(self, Sheep) == True:
            self.state = 0
            self.time = -1