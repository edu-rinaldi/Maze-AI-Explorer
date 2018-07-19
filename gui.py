import pygame



class MainWindow:
    width  = 100
    height = 100
    title = ""
    display = None
    bg = None
    pixelArray = None
    def __init__(self, title, bgFilename):
        self.title  = title
        self.bg = pygame.image.load(bgFilename)
        self.size = self.bg.get_rect().size
        self.display = pygame.display.set_mode(self.size)
        pygame.display.set_caption(title)
        self.setBg(self.bg,0,0)
        self.pixelArray = pygame.PixelArray(self.display)

    def _drawPixel(self, x, y, color):
        if 0<=x<self.size[0] and 0<=y<self.size[1]:
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

    def setBg(self,image,x,y):
        self.display.blit(image, (x, y))
        return self

if __name__=='__main__':
    pygame.init()
    window = MainWindow('labirinto','maze.png')

    run = True
    lsPixel = [(x,x) for x in range(window.size[0])]

    mouseDown = False
    while run:
        pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        if lsPixel != []:
            pos = lsPixel.pop(0)
            window.drawPixel(pos[0],pos[1], (255,0,0))
        pygame.display.update()

    pygame.quit()






