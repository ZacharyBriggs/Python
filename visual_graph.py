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
    '''Visual graph class for creating a list of visual nodes and drawing the nodes'''
    #Prototype: Visual_Graph()
    #Description: Creates a Visual_Graph object
    #Arguments: A regular graph and surface to drawn on
    #Precondition: None
    #Postcondition: A new visual graph is created
    #Protection: Public.
    def __init__(self, graph, surface):
        '''Creates a visual graph which is a collection of visual nodes'''
        self.vis_nodes = []
        self.graph = graph
        self.surface = surface
    
    #Prototype: create_vis_graph()
    #Description: Creates creates all the visual nodes in the visual graph
    #Arguments: None
    #Precondition: A visual graph
    #Postcondition: THe visual nodes in the visual graph are created
    #Protection: Public.
    def create_vis_graph(self):
        '''Creates all the visual_nodes in a graph'''
        counter = 0
        for x in range(8, self.graph.dimensions.x_pos * 60, 60):
            for y in range(8, self.graph.dimensions.y_pos * 60, 60):
                rect = Rectangle(Vector2(x,y), self.surface, (255,255,255), 45,45)
                new_node = Visual_Node(self.graph.nodes[counter], Vector2(x + (45 /2),y + (45/2)), rect)
                self.vis_nodes.append(new_node)
                counter += 1
    
    #Prototype: update()
    #Description: Updates all the vis nodes in the vis graph
    #Arguments: None
    #Precondition: Vis graph
    #Postcondition: All the vis nodes are created
    #Protection: Public.
    def update(self):
        '''Calls the update function for all the nodes in the graph'''
        for node in self.vis_nodes:
            node.update()
    
    #Prototype: draw_vis_graph()
    #Description: Draws all the vis nodes in the vis graph
    #Arguments: None
    #Precondition: vis graph
    #Postcondition: All the nodes in the vis graph are drawn
    #Protection: Public.
    def draw_vis_graph(self):
        '''Calls the draw function for all nodes in the graph'''
        for vis_node in self.vis_nodes:
            vis_node.draw(self)

    #Prototype: get_visual()
    #Description: Returns the visual node equal to the node inputted
    #Arguments: A node
    #Precondition: A node and vis graph
    #Postcondition: The visual node is returned if there is one equal to the node passed in
    #Protection: Public.
    def get_visual(self, node):
        '''Returns the visual node equal to the node inputted. Returns false if no visual node is equal to the node'''
        for visual in self.vis_nodes:
            if visual.node == node:
                return visual
        return None
    