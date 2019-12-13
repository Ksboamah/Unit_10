import pygame, sys
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Daily Exercises Creations")
main_surface.fill((255, 255, 255))

pygame.draw.polygon(main_surface, (102, 255, 255), ((100, 0), (0, 50), (50, 150), (150, 150), (200, 50)), 0)
pygame.draw.line(main_surface, (255, 0, 0), (50, 25), (100, 25), 4)
pygame.draw.line(main_surface, (255, 0, 0), (100, 25), (50, 75), 2)
pygame.draw.line(main_surface, (255, 0, 0), (50, 75), (100, 75), 4)
pygame.draw.rect(main_surface, (255, 255, 0), (125, 75, 100, 50), 0)
pygame.draw.circle(main_surface, (255, 0, 0), (250, 10), 20, 0)
pygame.draw.ellipse(main_surface, (255, 255, 0), (250, 150, 50, 100), 4)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
