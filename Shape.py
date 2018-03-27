from vector2 import Vector2
import pygame


class Shape(object):
    '''Shape class that stores values that all shapes use'''

    #Prototype: Shape()
    #Description: Creates a shape object
    #Arguments: A position
    #Precondition: None
    #Postcondition: A new Shape object is created
    #Protection: Public.
    def __init__(self, pos, surface, rgb):
        '''Creates a default Shape that has values that all shapes use'''
        self.pos = pos
        self.surface = surface
        self.color = rgb
    #Prototype: change_color()
    #Description: Changes the shape color to whats passed in
    #Arguments: None
    #Precondition: A Shape object
    #Postcondition: The shapes color is changed
    #Protection: Public.
    def change_color(self, rgb):
        '''Changes the shape color to whats passed in'''
        self.color = rgb

class Rectangle(Shape):
    '''Rectangle shape'''
    #Prototype: Rectangle()
    #Description: Creates a Rectangle object and a shape object
    #Arguments: A position, surface to draw on, color, width, and height
    #Precondition: None
    #Postcondition: A new Shape object and Rectangle object is created
    #Protection: Public.
    def __init__(self, pos, surface, rgb, width, height):
        '''Creates a rectangle shape'''
        Shape.__init__(self, pos, surface, rgb)
        self.rect = pygame.rect.Rect(pos.x_pos, pos.y_pos, width, height)

    #Prototype: draw()
    #Description: Draws the rectangle
    #Arguments: None
    #Precondition: A rectangle
    #Postcondition: The rectangle is drawn
    #Protection: Public.            
    def draw(self):
        '''Draws the rectangle'''
        pygame.draw.rect(self.surface, self.color, self.rect)

class Line(Shape):
    '''Line shape'''
    #Prototype: Line()
    #Description: Creates a Line object and a shape object
    #Arguments: A start, end, surface to draw on, color, and line thickness
    #Precondition: None
    #Postcondition: A new Shape object and Line object is created
    #Protection: Public.
    def __init__(self, start, end, surface, rgb, thickness):
        '''Creates a Line shape'''
        Shape.__init__(self, start, surface, rgb)
        self.start_point = start
        self.end_point = end
        self.thickness = thickness
    #Prototype: draw()
    #Description: Draws the Line
    #Arguments: None
    #Precondition: A line
    #Postcondition: The line is drawn
    #Protection: Public.
    def draw(self):
        '''Draws the line'''
        pygame.draw.line(self.surface, self.color, (self.start_point.x_pos, self.start_point.y_pos), (self.end_point.x_pos, self.end_point.y_pos), self.thickness)

class Lines(Shape):
    '''Connected lines shape'''

    #Prototype: Lines()
    #Description: Creates a Lines object and a shape object
    #Arguments: A surface to draw on, color, and a list of positions
    #Precondition: None
    #Postcondition: A new Shape object and Lines object is created
    #Protection: Public.
    def __init__(self, surface, rgb, pos_list):
        '''Creates a Lines shape'''
        Shape.__init__(self, pos_list, surface, rgb)
        self.color = rgb
        self.point_list = pos_list

    #Prototype: draw()
    #Description: Draws the lines
    #Arguments: None
    #Precondition: A lines object
    #Postcondition: Draws lines from one position to another
    #Protection: Public.
    def draw(self):
        '''Draws the lines'''
        pygame.draw.lines(self.surface, self.color, False, self.point_list)
        
class Text(Shape):
    '''Text class'''

    #Prototype: Text()
    #Description: Creates a Text object and a shape object
    #Arguments: A string of text, font, position, surface to draw on, and color
    #Precondition: None
    #Postcondition: A new Shape object and Text object is created
    #Protection: Public.
    def __init__(self, text, font, pos, surface, rgb):
        '''Creates a text shape '''
        Shape.__init__(self, pos, surface, rgb)
        self.text = text
        self.font = font

    #Prototype: draw()
    #Description: Draws the text
    #Arguments: None
    #Precondition: Text object
    #Postcondition: The text is drawn to the screen
    #Protection: Public.
    def draw(self):
        '''Draws the text'''
        screen = self.font.render(self.text, False, self.color)
        self.surface.blit(screen, (self.pos.x_pos, self.pos.y_pos))
        
class Circle(Shape):
    '''Circle shape'''
    #Prototype: Circle()
    #Description: Creates a Circle object and a shape object
    #Arguments: A position, surface to draw on, color, and a radius
    #Precondition: None
    #Postcondition: A new circle object and Shape object is created
    #Protection: Public.
    def __init__(self, pos, surface, rgb, radius):
        '''Creates a circle shape'''
        Shape.__init__(self, pos, surface, rgb)
        self.radius = radius
    #Prototype: draw()
    #Description: Draw the Circle object
    #Arguments: None
    #Precondition: A circle object
    #Postcondition: THe circle is drawn
    #Protection: Public.
    def draw(self):
        '''Draws the circle'''
        pygame.draw.circle(self.surface, self.color, (self.pos.x_pos, self.pos.y_pos), self.radius)