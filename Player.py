import random
from utils import *

class Player:
    fitness = 0
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    canwalk = True
    win = False
    def __init__(self, init, end, maze,bp):
        self.path = [init]
        self.maze = maze
        self.end = end
        self.color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        self.bestpath = bp
        self.maxdistance = len(bp)
        #self.maxdistance = manhattan(init[1],init[0],end[1],end[0])

    def __str__(self):
        return str(self.path)+" Fitness: "+str(self.fitness)

    def _inside(self,y,x):
        return 0<=x<self.maze.width and 0<=y<self.maze.height

    def _getnewpos(self, d):
        return self.path[-1][0]+d[0], self.path[-1][1]+d[1]

    def _isvaliddir(self, d):
        newpos = self._getnewpos(d)
        return self._inside(newpos[0],newpos[1]) and self.maze.getMaze()[newpos[0]][newpos[1]] == (255,255,255) and newpos not in self.path

    def onestep(self):
        if self.canwalk:
            validDirections = list(filter(lambda d: self._isvaliddir(d),self.dirs))
            if len(validDirections)>0:
                self.path.append(self._getnewpos(random.choice(validDirections)))
                if self.path[-1] == self.end:
                    self.canwalk = False
                    self.win = True
            else:
                self.canwalk = False

    def walk(self):
        while self.canwalk:
            self.onestep()

    def evaluate(self):
        self.walk()
        lp = self.path[-1]
        distance = len(pathfinding(lp,self.end,self.maze.getMaze())) if not self.win else 0
        # distance = manhattan(lp[1],lp[0], self.end[1], self.end[0])
        self.fitness = mapFromTo(distance*distance, self.maxdistance*self.maxdistance, 0, 0, 1)

    def crossover(self, partner):
        child = Player(self.path[0],self.end, self.maze, self.bestpath)
        maxParent = max(self,partner,key=lambda x: x.fitness)
        index = 80*len(maxParent.path)//100
        child.path = maxParent.path[:index]
        # child.path = maxParent.path[:int(mapFromTo(random.random(),0,1,1,len(maxParent.path)))]
        return child

    def mutate(self):
        self.path = self.path[:int(mapFromTo(random.random(),0,1,1,len(self.path)))]




