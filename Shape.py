from vector2 import Vector2
import pygame

class Shape(object):
    def __init__(self, pos, surface, rgb):
        ''''''
        self.pos = pos
        self.surface = surface
        self.color = rgb
    def change_color(self, rgb):
        '''Changes the shape color to whats passed in'''
        self.color = rgb

class Rectangle(Shape):
    def __init__(self, pos, surface, rgb, width, height):
        '''Creates a rectangle shape'''
        Shape.__init__(self, pos, surface, rgb)
        self.rect = pygame.rect.Rect(pos.x_pos, pos.y_pos, width, height)            
    def draw(self):
        '''Draws the rectangle'''
        pygame.draw.rect(self.surface, self.color, self.rect)

class Line(Shape):
    def __init__(self, start, end, surface, rgb, thickness):
        '''Creates a Line shape'''
        Shape.__init__(self, start, surface, rgb)
        self.start_point = start
        self.end_point = end
        self.thickness = thickness
    def draw(self):
        '''Draws the line'''
        pygame.draw.line(self.surface, self.color, (self.start_point.x_pos, self.start_point.y_pos), (self.end_point.x_pos, self.end_point.y_pos), self.thickness)

class Lines(Shape):
    def __init__(self, surface, rgb, pos_list):
        '''Creates a Lines shape'''
        Shape.__init__(self, pos_list, surface, rgb)
        self.color = rgb
        self.point_list = pos_list
    def draw(self):
        '''Draws the lines'''
        pygame.draw.lines(self.surface, self.color, False, self.point_list)
        
class Text(Shape):
    def __init__(self, text, font, pos, surface, rgb):
        '''Creates a text shape'''
        Shape.__init__(self, pos, surface, rgb)
        self.text = text
        self.font = font
    def draw(self):
        '''Draws the text'''
        screen = self.font.render(self.text, False, self.color)
        self.surface.blit(screen, (self.pos.x_pos, self.pos.y_pos))
        
class Circle(Shape):
    def __init__(self, pos, surface, rgb, radius):
        '''Creates a circle shape'''
        Shape.__init__(self, pos, surface, rgb)
        self.radius = radius
    def draw(self):
        '''Draws the circle'''
        pygame.draw.circle(self.surface, self.color, (self.pos.x_pos, self.pos.y_pos), self.radius)