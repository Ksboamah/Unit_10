import brick
import pygame, sys
from pygame.locals import *


def main():
    main_surface = pygame.display.set_mode((230, 220), 0, 32)
    main_surface.fill((255, 255, 255))
    red_brick = brick.Brick(main_surface, 20, 20, (255, 0, 0))
    blue_brick = brick.Brick(main_surface, 20, 20, (0, 0, 255))
    green_brick = brick. Brick(main_surface, 20, 20, (0, 255, 0))
    orange_brick = brick. Brick(main_surface, 20, 20, (255, 128, 0))
    yellow_brick = brick. Brick(main_surface, 20, 20, (255, 255, 0))
    space = 5
    width = 20
    for x in range(9):
        red_brick.draw((space + ((width + space) * x)), (220 - width - space))
    for x in range(7):
        orange_brick.draw((width + (1.3 * space) + (space + ((width + space) * x))), (220 - (2 * space) - (2 * width)))
    for x in range(5):
        yellow_brick.draw((width * 1.5 + (4 * space) + (space + ((width + space) * x))), (220 - (3 * space) - (3 * width)))
    for x in range(3):
        green_brick.draw((width * 2.3 + (6 * space) + (space + ((width + space) * x))), (220 - (4 * space) - (4 * width)))
    blue_brick.draw((width * 1.1 + (6 * space) + (space + ((width + space) * x))), (220 - (5 * space) - (5 * width)))



main()

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


