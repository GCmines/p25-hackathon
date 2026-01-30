from entities2 import Animal, Sheep, Wolf, Grass
import random as rd
from grid_copy import Grid
import pyxel 
import time 

def game(MAX_TURNS=500):
    
    # Initialisation des paramètres
    grid_size = 30
    nb_sheep_init = 50
    nb_wolves_init = 10
    grass_proportion_init = 30
    nb_grass_init = int(grass_proportion_init/100*grid_size**2)

    # Energy
    sheep_initial_energy = 20
    wolf_initial_energy = 40
    sheep_energy_loss_per_turn = 1
    wolf_energy_loss_per_turn = 2
    sheep_energy_from_grass = 15
    wolf_energy_from_sheep = 35

    # Reproduction
    reproduction_energy_cost = 20
    sheep_reproduction_threshold = 50
    wolf_reproduction_threshold = 80
    # Age
    sheep_max_age = 50
    wolf_max_age = 40

    '''
    # Herbe                                         # CES PARAMETRES SONT OBSOLETES AVEC LA PRESENCE DES SAISONS
    grass_regrowth_time = 7
    grass_growth_probability = 0.08
    '''
    
    
    
    ## Initialisation de la grille
    grass_grid = [[Grass(0, 0) for i in range(grid_size)]for j in range(grid_size)]     # Calque pour le sol/l'herbe
    animal_grid = [[0 for i in range(grid_size)]for j in range(grid_size)]       # Calque pour les animaux
    
    if nb_sheep_init + nb_wolves_init > grid_size**2:                                   # Le nombre d'animaux à l'état initial ne peut pas dépasser la taille de la grille
        return False
    else:
        tempcoord = [[(i,j) for j in range(grid_size)] for i in range(grid_size)]       # Calque temporaire donnant les coordonnées des cases de la grille
        tempnumb = []                                                                   # Calque temporaire donnant le numéro des cases de la grille
        for ligne in tempcoord :
            for nb in ligne:
                tempnumb.append(nb)                                                             # la boucle for sert juste à donner un numéro à chaque case

        whereanimals = rd.sample(tempnumb, nb_sheep_init + nb_wolves_init)              # On attribue de façon aléatoire une position sur la grille aux animaux (peu importe le type d'animal)
        wheresheep = rd.sample(whereanimals, nb_sheep_init)                             # Parmi ces numéros, on précise lesquels sont pour les moutons
        for i,j in wheresheep:                                                          # On place les moutons sur les cases qui leur ont été attribuées
            animal_grid[i][j] = Sheep(position=(i,j), age=0, energy=sheep_initial_energy)
        for i,j in whereanimals:                                                        # On met les loups sur les cases restantes
            if (i,j) not in wheresheep:
                animal_grid[i][j] = Wolf(position=(i,j), age=0, energy=wolf_initial_energy)
        
        Wheregrass = rd.sample(tempnumb, nb_grass_init)                                 # On attribue de façon aléatoire des cases pour l'herbe
        for i,j in tempnumb:                                                            # On place du sol vide avec un état de repousse aléatoire
            temps = rd.randint(0, 6)
            grass_grid[i][j] = Grass(0, temps)
        for i,j in Wheregrass:                                                          # On place de l'herbe, en pensant à mettre son état de repousse à 0
            grass_grid[i][j].state = 1
            grass_grid[i][j].time = 0

    initgrid = Grid(grid_size, grass_grid, animal_grid)                                     # Maintenant que nos calques sont prêts, on fabrique l'objet Grid les comprenant


    pyxel.init(grid_size, grid_size, title = "Ecosystème", fps = 10)
    turn_number = 0
    grid = initgrid

    def update():
        number_of_animals = 1
        nonlocal turn_number, grid
        #while (turn_number < MAX_TURNS) and (number_of_animals>0):
        turn_number += 1
        if turn_number <= MAX_TURNS:
            grid = tour(grid, MAX_TURNS, turn_number, grid_size, sheep_energy_from_grass, wolf_energy_from_sheep, sheep_max_age, wolf_max_age, sheep_energy_loss_per_turn, wolf_energy_loss_per_turn, sheep_reproduction_threshold, wolf_reproduction_threshold, reproduction_energy_cost)
    
        
    def draw():
        pyxel.cls(0)
        for a in range(grid_size):
            for b in range(grid_size):
                if isinstance(grid.animals[a][b], Sheep):
                    pyxel.pset(a,b,7)
                elif isinstance(grid.animals[a][b], Wolf):
                    pyxel.pset(a,b,13)
                elif (grid.grass[a][b].state == 1):
                    pyxel.pset(a,b,11) 
                else :
                    pyxel.pset(a,b,9)

    pyxel.run(update, draw)





def tour(grid, nbmaxtours, touractuel, size, sheepgain, wolfgain, sma, wma, stc, wtc, sthr, wthr, cst):
    
    
    #time.sleep(1)
        
    # PHASE 1 : INCREMENT DE L'AGE DES ANIMAUX
    for ligne in grid.animals:
        for animal in ligne:
            if isinstance(animal, Sheep):
                animal.gettin_old(sma)
            elif isinstance(animal, Wolf):
                animal.gettin_old(wma)
                                    
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
    for x in range(size):                                                           # On repère les outons sur la grille
        for y in range(size):
            if isinstance(grid.animals[x][y], Sheep):
                current_sheep = grid.animals[x][y]
                current_sheep.deplacement(grid, size, sheepgain)      # déplace et alimente les moutons
                current_sheep.energy_natural_loss(stc)

    # PHASE 4 : LOUPS
    for x in range(size):
        for y in range(size):
            if isinstance(grid.animals[x][y], Wolf):
                current_wolf = grid.animals[x][y]
                current_wolf.deplacement(grid, size, wolfgain)
                current_wolf.energy_natural_loss(wtc)

    # PHASE 5 : VERIFICATION DES MORTS
    for ligne in grid.animals:
        for animal in ligne:
            if isinstance(animal, Sheep):
                animal.death_verification(sma, grid)
            if isinstance(animal, Wolf):
                animal.death_verification(wma, grid)

    # PHASE 6 : REPRODUCTION
    for ligne in grid.animals:
        for animal in ligne:
            if isinstance(animal, Sheep):
                animal.reproduction(grid, size, sthr, cst, Sheep)
            if isinstance(animal, Wolf):
                animal.reproduction(grid, size, wthr, cst, Wolf)

    # PHASE 8 : VÉRIFICATION DES CONDITIONS D'ARRÊT
    number_of_animals = 0                                                                       # On reset notre compteur d'animaux
    for ligne in grid.animals:                                                                  # On parcourt les x et y
        for animal in ligne:
            if isinstance(animal, Sheep) or isinstance(animal, Wolf):                           # On regarde s'il y a des animaux sur notre grille
                number_of_animals += 1
    if number_of_animals == 0:                                                                  # S'il n'y a pas d'animaux, c'est la fin de la simulation
        endgame()

    return grid

def endgame():
    print("Fin de la simulation")
    pyxel.quit()



game(500)





