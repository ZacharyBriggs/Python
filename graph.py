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
    
    def __getiten__(self, index):
        return self.nodes[index]

    def print_graph(self, start_node, goal_node, path):
        graph_string = ""
        node_num = 0
        for node in self.nodes:
            if node.traversable is False:
                graph_string = "[X]" + graph_string
            elif node.position == start_node.position:
                graph_string = "[S]" + graph_string
            elif node.position == goal_node.position:
                graph_string = "[G]" + graph_string
            elif path.__contains__(node):
                 graph_string = "[@]" + graph_string
            else:            
                graph_string = "[ ]" + graph_string  
            if node.position.y_pos >= self.dimensions.y_pos - 1:
                graph_string = "\n" + graph_string
                print graph_string
                graph_string = ""
            node_num += 1