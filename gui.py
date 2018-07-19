import pygame, png, immagini
from Maze import Maze


class MainWindow:
    width  = 100
    height = 100
    blockSize = 10
    title = ""
    display = None
    bg = None
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

    def drawPixel(self, x, y, color):
        self._drawPixel(x,y,color)
        pygame.display.update()

    def drawRectangle(self, sx, sy, width, height, color):
        for y in range(sy,sy+height):
            for x in range(sx, sx+width):
                self._drawPixel(x,y, color)
        pygame.display.update()

    def drawImg(self,img, sx, sy):
        for y in range(len(img)):
            for x in range(len(img)):
                self._drawPixel(sx+x,sy+y, img[y][x])
    def drawMaze(self, img, gb):
        for y in range(0,len(img)*gb,gb):
            for x in range(0,len(img[0])*gb,gb):
                self.drawRectangle(x,y, gb,gb, img[y][x])

    def setBg(self,image,x,y):
        self.display.blit(image, (x, y))
        return self

if __name__=='__main__':
    pygame.init()
    maze = Maze(50, 50)

    window = MainWindow('labirinto',maze.width,maze.height)
    run = True
    drawn = set()
    queue = []
    while run:
        pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        mazeImg = maze.getMaze()
        coords = set(maze.getWay())
        coords.update(maze.getVisited())
        for y,x in coords:
            if (y,x) not in drawn:
                drawn.add((y,x))
                queue.append((y,x))
                window.drawRectangle(y*window.blockSize,x*window.blockSize,window.blockSize,window.blockSize,
                                      mazeImg[y][x])
        pygame.display.update()
        maze.workOneStep()


    pygame.quit()






