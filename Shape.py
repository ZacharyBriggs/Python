from vector2 import Vector2
import pygame

class Shape(object):
    def __init__(self, surface):
        self.surface = surface
        self.pygame_object = None
    def draw_square(self, r, g, b, pos, width, height):
        self.pygame_object = pygame.draw.rect(self.surface,(r, g, b),(pos.x_pos, pos.y_pos, width, height))
    def draw_line(self, pos):
        self.pygame_object = pygame.draw.line(self.surface, (0,0,255), pos.x_pos, pos.y_pos)
    def draw_path(self, pos):
        self.pygame_object = pygame.draw.rect(self.surface, (255,0,0), (pos.x_pos, pos.y_pos, 20, 20))

