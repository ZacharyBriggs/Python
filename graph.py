'''Graph class made up of nodes'''
from node import Node
from vector2 import Vector2
from shape import Shape
import pygame

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

    def draw_graph(self, astar, surface):    
        draw_pos = Vector2(0,0)
        shapes = Shape(surface)
        left_click, middle_click, right_click = pygame.mouse.get_pressed()
        clicked = False
        events = pygame.event.get()
        for node in self.nodes:
            shapes.draw_square(255,255,255,draw_pos, 20, 20)
            
            for close_node in astar.close_list:
                if node.position == close_node.position:
                    shapes.draw_square(100,30,150,draw_pos,20,20)
            if astar.path.__contains__(node):
                shapes.draw_square(255,0,0, draw_pos,20,20)
            for open_node in astar.open_list:
                if node.position == open_node.position:
                    shapes.draw_square(100,150,30,draw_pos,20,20)
            if node.traversable is False:
                shapes.draw_square(0,0,0,draw_pos,20,20)
            elif node.position == astar.start_node.position:
                shapes.draw_square(0,0,255,draw_pos,20,20)
            elif node.position == astar.goal_node.position:
                shapes.draw_square(0,255,0,draw_pos,20,20)
            if shapes.pygame_object.collidepoint(pygame.mouse.get_pos()) and left_click:
                node.toggle_traversable()
                clicked = left_click
            if shapes.pygame_object.collidepoint(pygame.mouse.get_pos()) and right_click:
                astar.goal_node = node
                astar.goal_node.is_goal = True
            draw_pos.x_pos += 25
            if node.position.y_pos >= self.dimensions.y_pos - 1:
                draw_pos.y_pos += 25
                draw_pos.x_pos = 0