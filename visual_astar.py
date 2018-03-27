from vector2 import Vector2
from graph import Graph
from astar import A_Star
from shape import Shape
from shape import Rectangle
from shape import Circle
from shape import Text
from shape import Line
from shape import Lines
from visual_node import Visual_Node
from visual_graph import Visual_Graph
import pygame

class Visual_Astar(object):
    '''Visual astar class for handling the astar algorithim and drawing the visual graph/nodes'''

    #Prototype: Visual_Astar()
    #Description: Creates a Visual_Astar object
    #Arguments: A graph object and a surface to draw on
    #Precondition: None
    #Postcondition: Visual Astar object is created
    #Protection: Public.
    def __init__(self, surface):
        '''Creates a class for controlling the astar algorithim'''
        self.algorithm = A_Star(18, 12)
        self.graph_visual = Visual_Graph(self.algorithm.search_area, surface)
        self.graph_visual.create_vis_graph()
        self.algorithm.pathfind(1, 100, self.algorithm.search_area)
        self.start_node = None
        self.goal_node = None
        
    #Prototype: update()
    #Description: Clears out the graph and calls algorithim's pathfind function
    #Arguments: None
    #Precondition: A visual astar object
    #Postcondition: Astar is updated and a new path is found
    #Protection: Public.
    def update(self):
        '''Updates/clears the graph and calls the path finding function'''
        self.set_goal()
        self.set_start()
        self.graph_visual.update()
        if pygame.key.get_pressed()[pygame.K_RETURN] != 0:
            for node in self.graph_visual.vis_nodes:
                node.reset_node()
            self.algorithm.pathfind(self.start_node.index, self.goal_node.index, self.graph_visual.graph)
            for node in self.algorithm.open_list:
                visual = self.graph_visual.get_visual(node)
                if visual is not None:
                    visual.is_open = True
            for node in self.algorithm.close_list:
                visual = self.graph_visual.get_visual(node)
                if visual is not None:
                    visual.is_closed = True
            for node in self.algorithm.path:
                visual = self.graph_visual.get_visual(node)
                if visual is not None:
                    visual.is_path = True
            self.algorithm.open_list = []
            self.algorithm.close_list = []
    
    #Prototype: draw()
    #Description: Calls the visual graphs draw function unless there is no path
    #Arguments: None
    #Precondition: A visual astar object
    #Postcondition: The graph is drawn
    #Protection: Public.
    def draw(self):
        '''Calls the visual graphs draw function unless there is no path'''
        if self.algorithm.path is None:
            return
        self.graph_visual.draw_vis_graph()
    
    #Prototype: set_start()
    #Description: Sets a node as the start node if the mouse collides with the node and the right mouse is clicked
    #Arguments: None
    #Precondition: A visual astar object
    #Postcondition: The node clicked is set as the start node
    #Protection: Public.
    def set_start(self):
        '''Sets a node as the start node if the mouse collides with the node and the right mouse is clicked'''
        for visual in self.graph_visual.vis_nodes:
            if visual.shape.rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[2]:
                    visual.set_as_start()
                    vis_start = self.graph_visual.get_visual(self.algorithm.start_node)
                    if vis_start is not None:
                        vis_start.is_start = False
                        vis_start.node.is_start = False
                    self.start_node = visual.node
                    print str(self.algorithm.start_node.position.x_pos) + "," + str(self.algorithm.start_node.position.y_pos)      
    
    #Prototype: set_goal()
    #Description: Sets a node as the goal node if the mouse collides with the node and the middle mouse is clicked
    #Arguments: None
    #Precondition: A visual astar object
    #Postcondition: The node clicked is set as the goal node
    #Protection: Public.
    def set_goal(self):
        '''Sets a node as the goal node if the mouse collides with the node and the middle mouse is clicked'''
        for visual in self.graph_visual.vis_nodes:
            if visual.shape.rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[1]:
                    visual.set_as_goal()
                    vis_goal = self.graph_visual.get_visual(self.algorithm.goal_node)
                    if vis_goal is not None:
                        vis_goal.is_goal = False
                        vis_goal.node.is_goal = False
                    self.goal_node = visual.node
                    print str(self.algorithm.goal_node.position.x_pos) + "," + str(self.algorithm.goal_node.position.y_pos)      
