from vector2 import Vector2
from graph import Graph
from shape import Rectangle
from shape import Lines
from shape import Line
import pygame

class Visual_Node(object):
    '''Visual node class that has various functions to change its values and an update function for checking nodes value and a draw function'''
    
    #Prototype: Visual_Node()
    #Description: Creates a visual node with the values passed in 
    #Arguments: A regular node, position, and shape
    #Precondition: None
    #Postcondition: A visual node is created
    #Protection: Public.
    def __init__(self, node, pos, shape):
        '''Creates a visual node with the node, pos, and shape passed in''' 
        self.node = node
        self.position = pos
        self.shape = shape
        self.is_start = False
        self.is_goal = False
        self.is_traversable = True
        self.is_path = False
        self.is_open = False
        self.is_closed = False

    #Prototype: update()
    #Description: Updates and changes the node's color if it hits any of the if statements also checks mouse clicks 
    #Arguments: None
    #Precondition:  A visual node
    #Postcondition: THe node is updated and its shapes color might be changed
    #Protection: Public.
    def update(self):
        '''Updates the node and changes its color if it is not traversable, start, goal, a path, in the open or close list'''
        if self.is_start:
            self.shape.change_color((0,255,0))
        elif self.is_goal:
            self.shape.change_color((255,0,0))
        elif not self.is_traversable:
            self.shape.change_color((0,0,0))
        elif self.is_path and (not self.is_goal or not self.is_start):
            self.shape.change_color((0,0,255))
        elif self.is_open and (not self.is_goal or not self.is_start):
            self.shape.change_color((125,125,155))
        elif self.is_closed and (not self.is_goal or not self.is_start):
            self.shape.change_color((155,125,125))
        else:
            self.shape.change_color((255,255,255))
        self.check_mouse_clicks()
    
    #Prototype: draw()
    #Description: Draws the node and a line connecting the node to its parent
    #Arguments: None
    #Precondition: A vector2
    #Postcondition: A vector2 is created
    #Protection: Public.
    def draw(self, vis_graph):
        '''Draws the shape and a line connecting the node to its parent'''
        self.shape.draw()
        if self.node.parent != None:
            if self.is_path is True:
                parent = vis_graph.get_visual(self.node.parent)
                parent_line = Line(self.position, parent.position, self.shape.surface, (150,255,25),1)
                parent_line.draw()
            else:
                parent = vis_graph.get_visual(self.node.parent)
                parent_line = Line(self.position, parent.position, self.shape.surface, (150,50,50),1)
                parent_line.draw()

    #Prototype: check_mouse_clicks()
    #Description: Checks if the mouse is colliding with a node and if left click was clicked
    #Arguments: None
    #Precondition: A node
    #Postcondition: The node is either made traversable or not traversable
    #Protection: Public.
    def check_mouse_clicks(self):
        '''Checks if the mouse is colliding with a node and if left click was clicked'''
        if self.shape.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.toggle_traversable()
    
    #Prototype: set_as_start()
    #Description: Sets the visual node's and its node's is_start to true
    #Arguments: None
    #Precondition: visual nodes is_start is false
    #Postcondition: visual nodes is_start is true
    #Protection: Public.
    def set_as_start(self):
        '''sets the visual node as the start and the node contained in it'''
        self.is_start = True
        self.node.is_start = True
    
    #Prototype: set_as_goal()
	#Description: Sets the visual node's and its node's is_start to true
	#Arguments: None
	#Precondition: visual nodes is_start is false
	#Postcondition: visual nodes is_start is true
	#Protection: Public.
    def set_as_goal(self):
        '''sets the visual node as the goal and the node contained in it'''
        self.is_goal = True
        self.node.is_goal = True

    #Prototype: toggle_traversable()
    #Description: Sets the visual node's and its node's traversable to true if it was false and vice versa
    #Arguments: None
    #Precondition: visual nodes traversable is false/true
    #Postcondition: visual nodes traversable is now the opposite
    #Protection: Public.
    def toggle_traversable(self):
        '''sets the visual node as not traversable and the node contained in it'''        
        self.node.toggle_traversable()
        self.is_traversable = self.node.traversable
    
    #Prototype: set_as_goal()
    #Description: Sets the visual node's propeties to 0/False
    #Arguments: None
    #Precondition: visual node has data in its properties
    #Postcondition: the properties are cleared out
    #Protection: Public.
    def reset_node(self):
        '''Clears out the visual node''' 
        self.node.g_score = 0
        self.node.h_score = 0
        self.node.f_score = 0
        self.node.parent = None
        self.is_open = False
        self.is_closed = False
        self.is_path = False