'''Graph class made up of nodes'''
from node import Node
from vector2 import Vector2
from shape import Shape

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
    
    def __getiten__(self, index):
        return self.nodes[index]
    
    def find_node(self, pos):
        for node in self.nodes:
            if node.position == pos:
                return node

    def draw_graph(self, start_node, goal_node, path, surface, cursor):    
        draw_pos = Vector2(0,0)
        shapes = Shape(surface)we cant ecveryone have some intelligence stats his is a -1 with a -10 mod
        for node in self.nodes:
            shapes.draw_node(draw_pos) 
            if node.traversable is False:
                shapes.draw_wall(draw_pos)
            if node.position == cursor.position:
                shapes.draw_cursor(draw_pos)
            elif node.position == start_node.position:
                shapes.draw_start(draw_pos)
            elif node.position == goal_node.position:
                shapes.draw_goal(draw_pos)
            elif path.__contains__(node):
                shapes.draw_path(draw_pos)
            draw_pos.x_pos += 25
            if node.position.y_pos >= self.dimensions.y_pos - 1:
                draw_pos.y_pos += 25
                draw_pos.x_pos = 0