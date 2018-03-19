from vector2 import Vector2
from graph import Graph
from astar import A_Star
from shape import Shape
from shape import Rectangle
from shape import Circle
from shape import Text
from shape import Line
from visual_node import Visual_Node
from visual_graph import Visual_Graph
import pygame

class Visual_Astar(object):
    def __init__(self, graph, surface):
        self.algorithm = A_Star(1, 99, graph)
        self.graph_visual = Visual_Graph(graph, surface)
        self.graph_visual.create_vis_graph()
        self.algorithm.pathfind(graph)

    def update(self, events):
        self.clear_searchspace()    
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
        self.graph_visual.update(events)
        if pygame.key.get_pressed()[pygame.K_RETURN] != 0:
            self.clear_searchspace()
            self.algorithm.pathfind(self.graph_visual.graph)

    def clear_searchspace(self):
        for node in self.graph_visual.vis_nodes:            
            node.is_path = False
            node.is_open = False
            node.is_closed = False

    def draw(self):
        self.graph_visual.draw_vis_graph()

    def set_start(self):
        for visual in self.graph_visual.vis_nodes:
            if visual.shape.rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[2]:
                    visual.set_as_start()
                    vis_start = self.graph_visual.get_visual(self.algorithm.start_node)
                    if vis_start is not None:
                        vis_start.is_start = False
                        vis_start.node.is_start = False
                    self.algorithm.start_node = visual.node
    
    def set_goal(self):
        for visual in self.graph_visual.vis_nodes:
            if visual.shape.rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[1]:
                    visual.set_as_goal()
                    vis_goal = self.graph_visual.get_visual(self.algorithm.goal_node)
                    if vis_goal is not None:
                        vis_goal.is_goal = False
                        vis_goal.node.is_goal = False
                    self.algorithm.goal_node = visual.node        

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
    screen.fill((0, 0, 0))
    events = pygame.event.get()
    for event in events:
        if event == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE] != 0:
            running = False 
        vis_star.update(events)
        vis_star.draw()        
        pygame.display.flip()
        pygame.display.update()