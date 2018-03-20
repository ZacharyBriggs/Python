from vector2 import Vector2
import pygame

class Shape(object):
    def __init__(self, pos, surface, rgb):
        self.pos = pos
        self.surface = surface
        self.color = rgb
    def change_color(self, rgb):
        self.color = rgb

class Rectangle(Shape):
    def __init__(self, pos, surface, rgb, width, height):
        Shape.__init__(self, pos, surface, rgb)
        self.rect = pygame.rect.Rect(pos.x_pos, pos.y_pos, width, height)            
    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)

class Line(Shape):
    def __init__(self, start, end, surface, rgb, thickness):
        Shape.__init__(self, start, surface, rgb)
        self.start_point = start
        self.end_point = end
        self.thickness = thickness
    def draw(self):
        pygame.draw.line(self.surface, self.color, (self.start_point.x_pos, self.start_point.y_pos), (self.end_point.x_pos, self.end_point.y_pos), self.thickness)

class Lines(Shape):
    def __init__(self, surface, rgb, pos_list):
        Shape.__init__(self, pos_list[0], surface, rgb)
        self.color = rgb
        self.point_list = pos_list
    def draw(self):
        pygame.draw.lines(self.surface, self.color, False, self.point_list)
        
class Text(Shape):
    def __init__(self, text, font, pos, surface, rgb):
        Shape.__init__(self, pos, surface, rgb)
        self.text = text
        self.font = font
    def draw(self):
        screen = self.font.render(self.text, False, self.color)
        self.surface.blit(screen, (self.pos.x_pos, self.pos.y_pos))
        
class Circle(Shape):
    def __init__(self, pos, surface, rgb, radius):
        Shape.__init__(self, pos, surface, rgb)
        self.radius = radius
    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.pos.x_pos, self.pos.y_pos), self.radius)