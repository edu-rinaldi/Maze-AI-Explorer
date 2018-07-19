import random


class GAPath:
    def __init__(self, initX, initY):
        randx, randy = initX+random.randrange(-1,1), initY+1+random.randrange(-1,1)
        self.path = [(initX,initY), (initX, initY+1)]
        if (randx,randy) not in self.path:
            self.path.append((randx,randy))
        self.fitness = -1
    def __str__(self):
        return "Path coords:\t"+str(self.path)+"\nFitness value:\t"+str(self.fitness)


def initPopulation(sizePopulation, initX, initY):
    return [GAPath(initX, initY) for _ in range(sizePopulation)]


def checkValidCoords(img,x,y):
    return img[y][x] == (255,255,255)


def distance(sx,sy,ex,ey):
    return abs(sx-ex) + abs(sy-ey)

def fitness(img, population, endX, endY):
    for element in population:
        coords = element.path[-1]
        element.fitness = -1 if not checkValidCoords(img, coords[0], coords[1]) else distance(coords[0],coords[1], endX, endY)
    return population


def ga(img, sizePopulation, gens, initX, initY, endX, endY):
    population = initPopulation(sizePopulation, initX, initY)
    for gen in range(gens):
        population = fitness(img, population, endX,endY)
        for pop in population:
            print(pop)


ga(0,10,1,10,0,20,20)


