from entities2 import Animal, Sheep, Wolf, Grass
import random as rd
from grid_copy import Grid
import pyxel 
import time 
GRID_SIZE = 30



def endgame():
    pyxel.quit()



def game(MAX_TURNS=500):
    
    # Initialisation des paramètres
    grid_size = 30
    sheep_initial_energy = 20
    wolf_initial_energy = 40
    SHEEP_ENERGY_LOSS_PER_TURN= 1
    REPRODUCTION_ENERGY_COST = 20
    SHEEP_REPRODUCTION_THRESHOLD = 50
    sheep_energy_from_grass = 15
    grass_regrowth_time = 7
    grass_growth_probability = 0.08
    SHEEP_MAX_AGE = 50
    WOLF_MAX_AGE = 40
    nb_sheep_init = 50
    nb_wolves_init = 10
    grass_proportion_init = 30
    nb_grass_init = int(grass_proportion_init/100*grid_size**2)
    
    ## Initialisation de la grille
    grass_grid = [[Grass(0, 0) for i in range(grid_size)]for j in range(grid_size)]     # Calque pour le sol/l'herbe
    animal_grid = [[Animal() for i in range(grid_size)]for j in range(grid_size)]       # Calque pour les animaux
    
    if nb_sheep_init + nb_wolves_init > grid_size**2:                                   # Le nombre d'animaux à l'état initial ne peut pas dépasser la taille de la grille
        return False
    else:
        Tempcoord = [[(i,j) for j in range(grid_size)] for i in range(grid_size)]       # Calque temporaire donnant les coordonnées des cases de la grille
        Tempnumb = []                                                                   # Calque temporaire donnant le numéro des cases de la grille
        for ligne in Tempcoord :
            for nb in ligne:
                Tempnumb.append(nb)                                                             # la boucle for sert juste à donner un numéro à chaque case

        Whereanimals = rd.sample(Tempnumb, nb_sheep_init + nb_wolves_init)              # On attribue de façon aléatoire une position sur la grille aux animaux (peu importe le type d'animal)
        Wheresheep = rd.sample(Whereanimals, nb_sheep_init)                             # Parmi ces numéros, on précise lesquels sont pour les moutons
        for i,j in Wheresheep:                                                          # On place les moutons sur les cases qui leur ont été attribuées
            animal_grid[i][j] = Sheep(position=(i,j), age=0, energy=sheep_initial_energy)
        for i,j in Whereanimals:                                                        # On met les loups sur les cases restantes
            if (i,j) not in Wheresheep:
                animal_grid[i][j] = Wolf(position=(i,j), age=0, energy=wolf_initial_energy)
        
        Wheregrass = rd.sample(Tempnumb, nb_grass_init)                                 # On attribue de façon aléatoire des cases pour l'herbe
        for i,j in Tempnumb:                                                            # On place du sol vide avec un état de repousse aléatoire
            temps = rd.random(0,6)
            grass_grid[i][j] = Grass(0, temps)
        for i,j in Wheregrass:                                                          # On place de l'herbe, en pensant à mettre son état de repousse à 0
            grass_grid[i][j].state = 1
            grass_grid[i][j].time = 0

    grid = Grid(grid_size, grass_grid, animal_grid)                                     # Maintenant que nos calques sont prêts, on fabrique l'objet Grid les comprenant


    pyxel.init(GRID_SIZE,GRID_SIZE,title = "Ecosystème",fps = 10)
    number_of_animals = 1
    turn_number = 0
    while (turn_number < MAX_TURNS) and (number_of_animals>0):
        turn_number += 1
        tour(grid, MAX_TURNS, turn_number, grid_size, sheep_energy_from_grass, wolf_energy_from_sheep)
        number_of_animals = 0
        for ligne in grid.ELT:
            for elt in ligne:
                if isinstance(elt, Sheep) or isinstance(elt, Wolf):
                    number_of_animals += 1
        pyxel.run(tour(grid),draw(grid,GRID_SIZE))
    
        
    endgame()





def tour(grid, nbmaxtours, touractuel, size, sheepgain, wolfgain):
    time.sleep(1)
    # PHASE 1 : INCREMENT DE L'AGE DES ANIMAUX
    for ligne in grid.animals:
        for elt in ligne:
            if isinstance(elt, Sheep) or isinstance(elt, Wolf):
                elt.age()
                
                                    
    # PHASE 2 : MISE A JOUR DE L'HERBE
    saison = nbmaxtours//4                                                  # On détermine le nombre de tours par saison
    if touractuel <= nbmaxtours:
                if touractuel < 3*saison:
                    if touractuel < 2*saison:
                        if touractuel < saison:                             # hiver
                            grass_regrowth_time = 7
                            grass_growth_probability = 0.08
                        else:                                               # printemps
                            grass_regrowth_time = 6
                            grass_growth_probability = 0.09
                    else:                                                   # été
                        grass_regrowth_time = 5
                        grass_growth_probability = 0.08
                else:                                                       # automne
                    grass_regrowth_time = 6
                    grass_growth_probability = 0.09
    for ligne in grid.grass:
        for case in ligne:
            case.eaten_grass()                                               # On regarde si l'herbe a été mangée
            case.new_grass(grass_growth_probability)                         # On regarde si l'herbe peut apparaitre aléatoirement
            case.regrowth(grass_regrowth_time)                               # On fait repousser l'herbe en fonction de son temps de repousse


    # PHASE 3 : MOUTONS

    for k in range(GRID_SIZE):
        for l in range(GRID_SIZE):
            # repérage des moutons dans la grille
            if isinstance(grid.ELT[k][l],Sheep):
                current_sheep = grid.ELT[k][l]
                current_sheep.deplacement(current_sheep,grid, size, sheepgain)   # déplace et alimente les moutons
                current_sheep.energy(current_sheep)

    # PHASE 4 : LOUPS
    for x in range(0, GRID_SIZE - 1):                                 
        for y in range(0, GRID_SIZE - 1):
            if isinstance(grid.ELT[x][y], Wolves):
                wolf = grid.ELT[x][y]
                wolf.age()
                wolf.mouvement()


    # PHASE 6 : REPRODUCTION
    for ligne in grid.ELT:
        for elt in ligne:
            if isinstance(elt, Sheep) or isinstance(elt, Wolves):
                elt.reproduction()


    # PHASE 8 : VÉRIFICATION DES CONDITIONS D'ARRÊT
    number_of_animals = 0                                                                       # On reset notre compteur d'animaux
    for ligne in grid.ELT:                                                                         # On parcourt les x et y
        for elt in ligne:
            if isinstance(elt, Sheep) or isinstance(elt, Wolves):         # On regarde s'il y a des animaux sur notre grille
                number_of_animals += 1
    if number_of_animals == 0:                                                                  # S'il n'y a pas d'animaux, c'est la fin de la simulation
        endgame()


## affichage graphique
def draw(grille,taille):
        for a in range(taille):
            for b in range(taille):
                if isinstance(grille.ELT[k][l],Sheep):
                    pyxel.pset(a,b,7)
                elif isinstance(grille.ELT[k][l],Wolves):
                    pyxel.pset(a,b,13)
                elif (grille.GRASS[a][b].STATE ==1):
                    pyxel.pset(a,b,11) 
                else :
                    pyxel.pset(a,b,9)
        
game(500)