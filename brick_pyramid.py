import brick
import pygame, sys
from pygame.locals import *


def main():
    main_surface = pygame.display.set_mode((500, 400), 0, 32)
    red_brick = brick.Brick(main_surface, 100, 100, (255, 0, 0))
    blue_brick = brick.Brick(main_surface, 100, 100, (255, 0, 0))

main()

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
