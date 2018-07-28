from Player import *

class GA:
    population = []
    bestp = []
    victory = False
    bestPlayer = None
    def __init__(self, gen, popsize, mr, init, end, maze):
        self.gen = gen
        self.curgen = 0
        self.popsize = popsize
        self.mr = mr
        self.init = init
        self.end = end
        self.bestp = pathfinding(init, end, maze.getMaze())
        self.initPopulation(init, end, maze)


    def initPopulation(self,init,end, maze):
        for i in range(self.popsize):
            self.population.append(Player(init, end, maze, self.bestp))
        self._fitness()


    def getMaxFitness(self):
        return max(map(lambda x: x.fitness,self.population))

    def _pickParent(self):
        maxFitness = self.getMaxFitness()
        while True:
            probParent = random.choice(self.population)
            r = random.uniform(0,maxFitness)
            if r <= probParent.fitness:
                break
        return probParent

    def _pickParents(self):
        self.population.sort(key=lambda p: p.fitness, reverse=True)
        parentA = self.population[0]
        parentB = self.population[1]
        return parentA,parentB

    def _fitness(self):
        for p in self.population:
            p.evaluate()

    def _selection(self):
        selected = []
        for i in range(self.popsize):
            # parentA = self._pickParent()
            # parentB = self._pickParent()
            parentA,parentB = self._pickParents()
            child = parentA.crossover(parentB)
            selected += [child]
        self.population = selected

    def _mutation(self):
        for p in self.population:
            if random.random() <= self.mr:
                p.mutate()


    def nextGen(self):
        self.curgen+=1

        #select and crossover
        self._selection()

        #mutation with certain probability
        self._mutation()

        # update fitness values for each path
        self._fitness()

        self.bestPlayer = max(self.population, key=lambda x: x.fitness)
        if self.bestPlayer.fitness==1:
            self.victory = True




