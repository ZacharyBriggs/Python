from vector2 import Vector2
import pygame

class Shape(object):
    def __init__(self, pos, surface, rgb):
        self.pos = pos
        self.surface = surface
        self.color = rgb
class Rectangle(object):
    def __init__(self, shape, scaler, width, height):
        self.scale = scaler
        self.rect(shape.surface, shape.color, shape.pos.x_pos, shape.pos.y_pos, width, height)
class Line(object):
    def __init__(self, shape, scaler, start, end):
        self.line(shape.surface, shape.color, start, end)
class Text(object):
class Circle(object):
    def __init__(self, shape, color)
    def __init__(self, surface):
        self.surface = surface
        self.pygame_object = None
    def draw_square(self, r, g, b, pos, width, height):
        self.pygame_object = pygame.draw.rect(self.surface,(r, g, b),(pos.x_pos, pos.y_pos, width, height))
    def draw_line(self, pos):
        self.pygame_object = pygame.draw.line(self.surface, (0,0,255), pos.x_pos, pos.y_pos)
    def draw_path(self, pos):
        self.pygame_object = pygame.draw.rect(self.surface, (255,0,0), (pos.x_pos, pos.y_pos, 20, 20))

