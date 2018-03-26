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
    def __init__(self, graph, surface):
        '''Creates a class for controlling the astar algorithim'''
        self.algorithm = A_Star(1, 99, graph)
        self.graph_visual = Visual_Graph(graph, surface)
        self.graph_visual.create_vis_graph()
        self.algorithm.pathfind(graph)
        
    #Prototype: update()
    #Description: Clears out the graph and calls algorithim's pathfind function
    #Arguments: None
    #Precondition: A visual astar object
    #Postcondition: Astar is updated and a new path is found
    #Protection: Public.
    def update(self):
        '''Updates/clears the graph and calls the path finding function'''
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
        self.set_goal()
        self.set_start()
        self.graph_visual.update()
        if pygame.key.get_pressed()[pygame.K_RETURN] != 0:
            for node in self.graph_visual.vis_nodes:
                node.reset_node()
            self.algorithm.pathfind(self.graph_visual.graph)
    
    #Prototype: draw()
    #Description: Finds the node at the position passed in
    #Arguments: A position
    #Precondition:A graph with the nodes created
    #Postcondition: The node at the position is returned
    #Protection: Public.
    def draw(self):
        '''Calls the visual graphs draw function unless there is no path'''
        self.graph_visual.draw_vis_graph()
        if self.algorithm.path is None:
            return

            
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
                    self.algorithm.start_node = visual.node
                    print str(self.algorithm.start_node.position.x_pos) + "," + str(self.algorithm.start_node.position.y_pos)      
    
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
                    self.algorithm.goal_node = visual.node
                    print str(self.algorithm.goal_node.position.x_pos) + "," + str(self.algorithm.goal_node.position.y_pos)      

height = 18
width = 12
pygame.init()
graph = Graph(Vector2(height,width))
graph.create_nodes()
screen = pygame.display.set_mode((1080, 720))
vis_graph = Visual_Graph(graph, screen)
running = True
vis_star = Visual_Astar(graph, screen)
while running:
    screen.fill((0, 0, 0))
    events = pygame.event.get()
    for event in events:
        if event == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE] != 0:
            running = False 
        vis_star.update()
        vis_star.draw()        
        pygame.display.flip()
        pygame.display.update()