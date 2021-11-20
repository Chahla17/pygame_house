import pygame
import sys

pygame.init()

WIDTH = 1440
HEIGHT = 850

class Square(object):
    def __init__(self, screen, left = 620, top = 325, width = 200, height = 200):
        self.left = left
        self.top = top
        self.width = width
        self.height = height 
        r = pygame.Rect(left, top, width, height)
        pygame.draw.rect(screen, (57, 255, 20), r, 1)

class Triangle(object):
    def __init__(self, screen, listpoint):
    
        pygame.draw.lines(screen, (57, 255, 20), True,
                  listpoint, 2)


screen = pygame.display.set_mode((WIDTH, HEIGHT))

Stena1 = Square(screen)
left = Stena1.left
top = Stena1.top
width = Stena1.width
height = Stena1.height
listpoint = [[left, top],[left + width/2, height],[left + width,top]]
Krisha = Triangle(screen, listpoint)





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
