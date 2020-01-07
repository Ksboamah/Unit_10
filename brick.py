import pygame

class Brick:

    def __init__(self, surface, brick_height, brick_width, brick_color):
        self.surface = surface
        self.height = brick_height
        self.width = brick_width
        self.color = brick_color

    def draw(self, location_x, location_y):
        pygame.draw.rect(self.surface, self.color, (location_x, location_y, self.width, self.height), 0)


