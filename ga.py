import random
from Maze import Maze
import immagini

class GAPath:
    #(x,y)
    offset = [(0,1),(0,-1),(1,0),(-1,0)]
    def __init__(self, initX, initY, endX, endY):
        self.fitness = 0
        self.path = [(initX, initY)]
        self.penalita = 0
        self.end = (endX, endY)
    def __str__(self):
        return "Fitness:\t"+str(self.fitness)+"\tCur coords:\t"+str(self.getCurrentCoords())+"\tPenalita':\t"+str(self.penalita)

    def getCurrentCoords(self):
        return self.path[-1]

    def distance(self):
        return abs(self.getCurrentCoords()[0] - self.end[0]) + abs(self.getCurrentCoords()[1] - self.end[1])

def initPopulation(n,init,end):
    """initialize population with starting and ending points"""
    return [GAPath(init[0],init[1],end[0],end[1]) for _ in range(n)]


def fitness(population, maze):
    """"""
    width, height = len(maze[0]), len(maze)
    for element in population:
        x,y = random.choice(GAPath.offset)
        cx, cy = element.getCurrentCoords()
        if not (0<=cx+x<width and 0<=cy+y<height) or maze[cy+y][cx+x] == (0,0,0) or (cx+x,cy+y) in element.path:
            element.penalita -= 10
        else:
            element.path.append((cx+x, cy+y))

        for ox, oy in GAPath.offset:
            cx, cy = element.getCurrentCoords()
            f = False
            if (0<=cx+ox<width and 0<=cy+oy<height) and maze[cy+oy][cx+ox] == (255,255,255) and not (cx+ox,cy+oy) in element.path:
                element.penalita += 20
                f = True
            element.penalita -= 10 if not f else 0

        element.fitness = element.distance() + element.penalita
    return population

def selection(population, npop):
    population.sort(key=lambda x: x.fitness, reverse=True)

    population = population[:int(npop*0.2)]
    return population

def crossover(population, npop, init, end):
    for _ in range(npop-len(population)):
        parent = random.choice(population)
        parent2 = random.choice(population)

        child = GAPath(init[0],init[1],end[0],end[1])
        child.path = [x for x in parent.path if x in parent2.path]
        # if len(parent.path)>1:
        #     child.path = parent.path[:int(len(parent.path)*random.uniform(0.5,1))]
        population.append(child)
    return population

def mutation(population):
    for element in population:
        if len(element.path)>1 and random.random()<= 0.002:
            randomIndex = int(len(element.path)*random.uniform(0.3,1))
            element.path = element.path[:randomIndex]
    return population

def ga(npop,gens,maze,init,end):

    population = initPopulation(npop,init,end)
    for gen in range(gens):
        #calcolo fitness value
        population = fitness(population, maze)
        #selezione
        population = selection(population, npop)
        #l'accoppiamento
        population = crossover(population, npop, init, end)
        #mutazione
        population = mutation(population)

    population.sort(key=lambda x: x.fitness,reverse=True)
    return population

# maze = Maze(100,100)
# while len(maze.frontier)>0:
#     maze.workOneStep()
# immagini.save(maze.getMaze(),"maze.png")

#ga(20,20000,maze.getMaze(),(1,1),(98,98))