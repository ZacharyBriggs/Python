'''Graph class made up of nodes'''
from node import Node
from vector2 import Vector2

class Graph:
    '''Graph class that has a function for creation and for finding neighbors of a node'''
    def __init__(self, dimensions):
        '''Creates a graph with a width and height of a the dimensions Vector2 passed in and creates a list of nodes'''
        self.dimensions = dimensions
        self.nodes = []        
    def create_nodes(self):
        '''Creates a graph of nodes from the dimensions vector'''
        for x in range(0, self.dimensions.x_pos):            
            for y in range(0, self.dimensions.y_pos):                
                self.nodes.append(Node(Vector2(x, y)))
                
    def find_neighbors(self, current_pos):
        '''Finds all the neighbors adjacent to the current node and returns a list of the neighbors'''
        neighbors = []
        neighbor_pos = [] 
        neighbor_pos.append(current_pos + Vector2(-1, 1)) #Top Left
        neighbor_pos.append(current_pos + Vector2(0, 1)) #Top
        neighbor_pos.append(current_pos + Vector2(1, 1)) #Top Right
        neighbor_pos.append(current_pos + Vector2(-1, 0)) #Left
        neighbor_pos.append(current_pos + Vector2(1, 0)) #Right
        neighbor_pos.append(current_pos + Vector2(-1, -1)) #Bot Left
        neighbor_pos.append(current_pos + Vector2(0, -1)) #Bot
        neighbor_pos.append(current_pos + Vector2(1, -1)) #Bot Right
        for node in self.nodes:
            for pos in neighbor_pos:
                if node.position.x_pos == pos.x_pos and node.position.y_pos == pos.y_pos:
                    neighbors.append(node)
        return neighbors