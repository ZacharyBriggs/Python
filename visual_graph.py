from vector2 import Vector2
from graph import Graph
from astar import A_Star
from shape import Shape
from shape import Rectangle
from shape import Circle
from shape import Text
from shape import Line
from visual_node import Visual_Node
import pygame

class Visual_Graph(object):
    def __init__(self, graph, surface):
        self.vis_nodes = []
        self.graph = graph
        self.surface = surface

    def create_vis_graph(self):
        counter = 0
        for x in range(8, self.graph.dimensions.x_pos * 60, 60):
            for y in range(8, self.graph.dimensions.y_pos * 60, 60):
                rect = Rectangle(Vector2(x,y), self.surface, (255,255,255), 45,45)
                new_node = Visual_Node(self.graph.nodes[counter], Vector2(x + (45 /2),y + (45/2)), rect)
                self.vis_nodes.append(new_node)
                counter += 1
    
    def update(self, events):
        for node in self.vis_nodes:
            node.update(events)

    def draw_vis_graph(self):
        for vis_node in self.vis_nodes:
            vis_node.draw(self)

    def get_visual(self, node):
        for visual in self.vis_nodes:
            if visual.node == node:
                return visual
        return None