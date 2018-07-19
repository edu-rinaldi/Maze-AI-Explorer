import random

class Maze:
    wallRGB, wayRGB = (0, 0, 0), (255, 255, 255)
    offset = [(0, 2), (0, -2), (-2, 0), (2, 0)]

    def __init__(self, width, height):

        if width % 2 == 0: width += 1
        if height % 2 == 0: height += 1

        self.width = width
        self.height = height

        # generate an empty maze
        self.frontier = []
        self.visited = {(1, 1)}
        self.maze = []
        self.ways = []

        for y in range(self.height):
            row = []
            for x in range(self.width):
                if y % 2 + x % 2 < 2:
                    row.append(Maze.wallRGB)
                else:
                    row.append(Maze.wayRGB)
            self.maze.append(row)

        # pprint.pprint(self.maze)

        # starting position
        self._addWalls(1, 1)

    def _clamp(self, n, minN, maxN):
        return min(max(minN, n), maxN)

    def _addWalls(self, y, x):
        for o in Maze.offset:
            cell = (y + o[0], x + o[1])
            if self._range(cell[0], cell[1]) and cell not in self.visited and cell not in self.frontier and \
                    self.maze[cell[0]][cell[1]] == Maze.wayRGB:
                self.frontier.append(cell)

    def findVisitedNear(self, y, x):
        return [(o[0] + y, o[1] + x) for o in Maze.offset if (o[0] + y, o[1] + x) in self.visited]

    def _range(self, y, x):
        return 0 <= x < self.width and 0 <= y < self.height

    def work(self):
        while len(self.frontier) > 0:
            rand = random.randint(0, len(self.frontier) - 1)
            cell = self.frontier.pop(rand)

            near = self.findVisitedNear(cell[0], cell[1])
            inmaze = near[random.randint(0, len(near) - 1)]

            dy, dx = self._clamp(cell[0] - inmaze[0], -1, 1), self._clamp(cell[1] - inmaze[1], -1, 1)

            if dy != 0: self.maze[inmaze[0] + dy][inmaze[1]] = Maze.wayRGB
            if dx != 0: self.maze[inmaze[0]][inmaze[1] + dx] = Maze.wayRGB

            self.visited.add(cell)

            self._addWalls(cell[0], cell[1])

    def getMaze(self):
        return self.maze

    def getVisited(self):
        return self.visited

    def getFrontier(self):
        return self.frontier

    def getWay(self):
        return self.ways

    def workOneStep(self):
        if len(self.frontier) > 0:
            rand = random.randint(0, len(self.frontier) - 1)
            cell = self.frontier.pop(rand)

            near = self.findVisitedNear(cell[0], cell[1])
            inmaze = near[random.randint(0, len(near) - 1)]

            dy, dx = self._clamp(cell[0] - inmaze[0], -1, 1), self._clamp(cell[1] - inmaze[1], -1, 1)

            if dy != 0:
                self.maze[inmaze[0] + dy][inmaze[1]] = Maze.wayRGB
                self.ways.append((inmaze[0] + dy, inmaze[1]))
            if dx != 0:
                self.maze[inmaze[0]][inmaze[1] + dx] = Maze.wayRGB
                self.ways.append((inmaze[0], inmaze[1] + dx))
            self.visited.add(cell)

            self._addWalls(cell[0], cell[1])

    def _quad(self, x, y, w, h, img, color):
        for dy in range(h): img[y + dy] += [color for i in range(w)]

    def genImg(self, wb, hb):
        img = [[] for i in range(self.height * hb)]
        tx, ty = 0, 0

        for y in range(self.height):
            for x in range(self.width):
                self._quad(tx, ty, wb, hb, img, self.maze[y][x])
                tx += wb
            ty += hb
        return img