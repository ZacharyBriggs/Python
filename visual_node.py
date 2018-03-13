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

    def draw(self):
        self.shape.draw()
    
