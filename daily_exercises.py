import pygame, sys
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Daily Exercises Creations")
main_surface.fill((255, 255, 255))

pygame.draw.polygon(main_surface, (102, 255, 255), ((200, 0), (0,200), (100,400), (300, 400), (400, 200)), 0)
pygame.draw.line(main_surface, (255, 0, 0))

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
