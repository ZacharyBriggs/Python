from node import Node
from vector2 import Vector2

class Graph:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.nodes = []        
    def create_nodes(self):
        for x in range(0, self.dimensions.x_pos):            
            for y in range(0, self.dimensions.y_pos):                
                self.nodes.append(Node(Vector2(x, y),True))