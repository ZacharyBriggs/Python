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
        self.is_traversable = True
        self.is_path = False
        self.is_open = False
        self.is_closed = False

    def update(self, events):
        if self.is_start:
            self.shape.change_color((0,255,0))
        elif self.is_goal:
            self.shape.change_color((255,0,0))
        elif not self.is_traversable:
            self.shape.change_color((0,0,0))
        elif self.is_open and (not self.is_goal or not self.is_start):
            self.shape.change_color((125,125,155))
        elif self.is_closed and (not self.is_goal or not self.is_start):
            self.shape.change_color((155,125,125))
        else:
            self.shape.change_color((255,255,255))
        self.check_mouse_clicks()

    def draw(self):
        self.shape.draw()

    def check_mouse_clicks(self):
        if self.shape.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.toggle_traversable()
                
    def set_as_start(self):
        self.is_start = True
        self.node.is_start = True

    def set_as_goal(self):
        self.is_goal = True
        self.node.is_goal = True

    def toggle_traversable(self):
        self.node.toggle_traversable()
        self.is_traversable = self.node.traversable