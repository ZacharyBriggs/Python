'''Graph class made up of nodes'''
from node import Node
from vector2 import Vector2
from shape import Shape
import pygame

class Graph:
    '''Graph class that has a function for creation and for finding neighbors of a node'''
    #Prototype: Graph()
    #Description: Creates a graph object
    #Arguments: The graph's dimensions
    #Precondition: None
    #Postcondition: A graph is created
    #Protection: Public.
    def __init__(self, dimensions):
        '''Creates a graph with a width and height of a the dimensions Vector2 passed in and creates a list of nodes'''
        self.dimensions = dimensions
        self.nodes = []        
        
    #Prototype: create_nodes()
    #Description: Creates all the nodes needed for the graph
    #Arguments: None
    #Precondition: A graph
    #Postcondition: All the nodes needed for the graph are created
    #Protection: Public.
    def create_nodes(self):
        '''Creates a graph of nodes from the dimensions vector'''
        for x in range(0, self.dimensions.x_pos):            
            for y in range(0, self.dimensions.y_pos):                
                self.nodes.append(Node(Vector2(x, y)))
    
    #Prototype: .
    #Description: Overloads get index and returns the node at the index
    #Arguments: An int representing the index
    #Precondition: A graph with the nodes created
    #Postcondition: The node at the index is returned
    #Protection: Public.
    def __getiten__(self, index):
        '''Overloads get index and returns an int representing the index of a node'''
        return self.nodes[index]
    
    #Prototype: find_node()
    #Description: Finds the node at the position passed in
    #Arguments: A position
    #Precondition:A graph with the nodes created
    #Postcondition: The node at the position is returned
    #Protection: Public.
    def find_node(self, pos):
        '''Takes in a vector2 representing a nodes pos and if a nodes pos in the graph is equal to the pos passed it the node is returned'''
        for node in self.nodes:
            if node.position == pos:
                return node
    