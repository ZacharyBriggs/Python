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
                new_node = Visual_Node(self.graph.nodes[counter], rect)
                self.vis_nodes.append(new_node)
                counter += 1

    def draw_vis_graph(self):
        for vis_node in self.vis_nodes:
            vis_node.draw()

    def get_visual(self, node):
        for visual in self.vis_nodes:
            if visual.node == node:
                return visual
        return None

class Visual_Astar(object):
    def __init__(self, graph, surface):
        self.algorithm = A_Star(1, 99, graph)
        self.graph_visual = Visual_Graph(graph, surface)
        self.graph_visual.create_vis_graph()
        self.algorithm.pathfind(graph)

    def update(self, events):
        self.algorithm.pathfind(self.algorithm.graph)
        for node in self.algorithm.open_list:
            visual = self.graph_visual.get_visual(node)
            if visual is not None:
                visual.shape.color = (255, 0, 255)
        for node in self.algorithm.close_list:
            visual = self.graph_visual.get_visual(node)
            if visual is not None:
                visual.shape.color = (0, 255, 0)
        for node in self.algorithm.path:
            visual = self.graph_visual.get_visual(node)
            if visual is not None:
                visual.shape.color = (155, 255, 155)
        for visual in self.graph_visual.vis_nodes:
            if visual.shape.rect.collidepoint(pygame.mouse.get_pos()):
                for event in events:
                    if pygame.mouse.get_pressed()[0]:            
                        visual.toggle_traversable()
                        if visual.is_traversable == False:
                            visual.shape.color = (255, 255, 255)
                        else:
                            visual.shape.color = (0, 0, 0)
                    if pygame.mouse.get_pressed()[2]:            
                        visual.is_start = True
                        visual.node.is_start = True                        
                        if visual.is_start == True:
                            visual.shape.color = (0, 0, 255)
                        else:
                            visual.shape.color = (0, 0, 0)
                    if pygame.mouse.get_pressed()[1]:
                        visual.is_goal = True
                        visual.node.is_goal = True
                        old = self.graph_visual.get_visual(self.algorithm.goal_node)
                        if old is not None:
                            old.is_goal = False
                            old.shape.color = (255, 255, 255)
                        self.algorithm.goal_node = visual.node
                        if visual.is_goal == True:
                            visual.shape.color = (255,0,0)    
        start = self.graph_visual.get_visual(self.algorithm.start_node)
        if start is not None:
            start.shape.color = (0, 0, 255)
        goal = self.graph_visual.get_visual(self.algorithm.goal_node)
        if goal is not None:
            goal.shape.color = (255, 0, 0)

    def draw(self):
        self.graph_visual.draw_vis_graph()
        
start = 70
goal = 45
height = 18
width = 18
pygame.init()
graph = Graph(Vector2(height,width))
graph.create_nodes()
graph.nodes[start].is_start = True
graph.nodes[goal].is_goal = True
font = pygame.font.SysFont('Chiller', 300)
screen = pygame.display.set_mode((1080, 720))
vis_graph = Visual_Graph(graph, screen)
running = True
astar = A_Star(start, goal, graph)
path = astar.pathfind(graph)
vis_star = Visual_Astar(graph, screen)
while running:
    events = pygame.event.get()
    for event in events:
        if event == pygame.QUIT:
            running = False 
    
    vis_star.update(events)
    vis_star.draw()
    pygame.display.update()        
    pygame.display.flip()