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
    def create_vis_graph(self, astar):
        list_shapes = []
        list_num = 0
        draw_pos = Vector2(0,0)
        for node in self.graph.nodes:            
            list_shapes.append(Rectangle(draw_pos, self.surface,(255,255,255),25,25))
            self.vis_nodes.append(Visual_Node((node.position), list_shapes[list_num]))
            for close_node in astar.close_list:
                if close_node.position == node.position:
                    list_shapes.append(Rectangle(draw_pos, self.surface,(200,150,100),25,25))
            for open_node in astar.open_list:
                if open_node.position == node.position:
                    list_shapes.append(Rectangle(draw_pos, self.surface,(100,200,100),25,25))
            if node.is_start is True:
                self.vis_nodes[list_num].is_start = True
                list_shapes.append(Rectangle(draw_pos, self.surface,(0,255,0),25,25))
            elif node.is_goal is True:
                self.vis_nodes[list_num].is_goal = True
                list_shapes.append(Rectangle(draw_pos, self.surface,(0,0,255),25,25))
            elif astar.path.__contains__(node):
                list_shapes.append(Rectangle(draw_pos, self.surface,(100,150,200),25,25))
            draw_pos.x_pos += 30
            list_num += 1
            if node.position.y_pos >= self.graph.dimensions.y_pos - 1:
                draw_pos.y_pos += 30
                draw_pos.x_pos = 0
        a = 0

    def draw_vis_graph(self):
        for vis_node in self.vis_nodes:
            vis_node.draw()

start = 70
goal = 45
height = 10
width = 10
pygame.init()
graph = Graph(Vector2(height,width))
graph.create_nodes()
graph.nodes[start].is_start = True
graph.nodes[goal].is_goal = True
font = pygame.font.SysFont('Chiller', 300)
screen = pygame.display.set_mode((1080, 720))
vis_graph = Visual_Graph(graph, screen)
a = Rectangle(Vector2(100,100), screen, (255,255,255), 35,35)
vis_node = Visual_Node(graph.nodes[24], a)
'''b = Circle(Vector2(300,300), screen, (255,255,255), 35)
c = Line(Vector2(400,200), Vector2(200,400), screen, (255,255,255), 10)
d = Text('Test', font, Vector2(500,500),screen,(255,255,255))'''

running = True
while running:
    astar = A_Star(start, goal, graph)
    path = astar.pathfind(graph)
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
    vis_graph.create_vis_graph(astar)
    vis_graph.draw_vis_graph()
    pygame.display.flip()
