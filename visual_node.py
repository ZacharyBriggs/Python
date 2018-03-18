from vector2 import Vector2
from graph import Graph
from shape import Shape
from shape import Rectangle
from shape import Circle
from shape import Text
from shape import Line
import pygame

class Visual_Node(object):
    def __init__(self, node, shape):
        self.node = node
        self.shape = shape
        self.is_start = False
        self.is_goal = False
        self.is_traversable = False

    def draw(self):
        self.shape.draw()

    def check_mouse_clicks(self, event, old_node, algorithm):
        if pygame.mouse.get_pressed()[0]:            
            self.toggle_traversable()
        if pygame.mouse.get_pressed()[2]:            
            self.is_start = True
            self.node.is_start = True                        
            if self.is_start == True:
                self.shape.change_color((0, 0, 255))
            else:
                self.shape.change_color((0, 0, 0))
        if pygame.mouse.get_pressed()[1]:
            self.is_goal = True
            self.node.is_goal = True
            if old_node is not None:
                old_node.is_goal = False
                old_node.shape.change_color((255, 255, 255))
            algorithm.goal_node = self.node
            if self.is_goal == True:
                self.shape.change_color((255,0,0))
                
    def toggle_traversable(self):
        if self.is_traversable == True:
            self.is_traversable = False
            self.shape.change_color((255,255,255))
        else:
            self.is_traversable = True
            self.shape.change_color((0,0,0))
        self.node.toggle_traversable()