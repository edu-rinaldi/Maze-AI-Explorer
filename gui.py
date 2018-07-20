import pygame, png, immagini
from Maze import Maze


class MainWindow:
    width = 100
    height = 100
    blockSize = 5
    title = ""
    display = None
    pixelArray = None
    def __init__(self, title, width, height):
        self.title  = title
        self.width = width*self.blockSize
        self.height = height*self.blockSize
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

if __name__=='__main__':
    pygame.init()
    maze = Maze(200, 200)

    window = MainWindow('labirinto', maze.width, maze.height)
    run = True
    while run:
        pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        for y,x in maze.getToDraw():
            window.drawRectangle(y*window.blockSize, x*window.blockSize, window.blockSize, window.blockSize, maze.getColor(y, x))
        pygame.display.update()
        maze.workOneStep()


    pygame.quit()
