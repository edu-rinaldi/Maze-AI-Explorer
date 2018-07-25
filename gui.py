import pygame
from Maze import Maze
from ga import *

class MainWindow:
    width = 100
    height = 100
    blockSize = 10
    title = ""
    display = None
    pixelArray = None
    maze = None
    def __init__(self, title, width, height):
        self.title  = title
        self.maze = Maze(width, height)
        self.width = self.maze.width*self.blockSize
        self.height = self.maze.height*self.blockSize
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)
        self.pixelArray = pygame.PixelArray(self.display)

    def _drawPixel(self, x, y, color):
        if 0<=x<self.width and 0<=y<self.height:
            self.pixelArray[x, y] = color

    def drawRectangle(self, sx, sy, width, height, color):
        for y in range(sy,sy+height):
            for x in range(sx, sx+width):
                self._drawPixel(x,y, color)
        pygame.display.update()
    def genMaze(self):
        genMaze = True
        while genMaze:
            pygame.time.Clock()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    genMaze = False
                    break
            for y, x in self.maze.getToDraw():
                self.drawRectangle(x * self.blockSize, y * self.blockSize, self.blockSize, self.blockSize,
                                     self.maze.getColor(y, x))
            if len(self.maze.frontier) == 0:
                genMaze = False
                break
            pygame.display.update()
            self.maze.workOneStep()
if __name__=='__main__':
    pygame.init()
    window = MainWindow('labirinto', 50,50)
    window.genMaze()

    ga = GA(100, 200, 0.01, (1,1), (49,49), window.maze)

    run = True

    while run:
        pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    """QUI VA GESTITO IL RESET CON IL TASTO R"""
        # for y,x in p:
        #     window.drawRectangle(x * window.blockSize, y * window.blockSize, window.blockSize, window.blockSize,
        #                          (34,45,23))
        ga.nextGen()
        for p in ga.population:
            #print(path.walk, path.directions)
            for y,x in p.path:
                window.drawRectangle(x*window.blockSize, y*window.blockSize, window.blockSize, window.blockSize, p.color)
        pygame.display.update()

    pygame.quit()
