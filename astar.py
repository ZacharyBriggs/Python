'''The A_Star pathfinding class'''
from vector2 import Vector2
from node import Node
from graph import Graph
from shape import Shape
import pygame

class A_Star:
    def __init__(self, start, goal, graph):
        '''Initilizes the A_Star class and creates an open_list, close_list, sets the start_node, and goal_node'''
        self.open_list = []
        self.close_list = []  
        self.neighbors = []
        self.path = []
        self.start_node = graph.nodes[start]
        self.start_node.is_start = True
        self.goal_node = graph.nodes[goal]
        self.goal_node.is_goal = True
        self.open_list.append(graph.nodes[start])

    def find_neighbors(self, graph, current_pos):
        '''Finds all the neighbors adjacent to the current node and returns a list of the neighbors'''
        neighbors = []
        neighbor_pos = [] 
        neighbor_pos.append(current_pos + Vector2(-1, 1)) #Top Left
        neighbor_pos.append(current_pos + Vector2(0, 1)) #Top
        neighbor_pos.append(current_pos + Vector2(1, 1)) #Top Right
        neighbor_pos.append(current_pos + Vector2(-1, 0)) #Left
        neighbor_pos.append(current_pos + Vector2(1, 0)) #Right
        neighbor_pos.append(current_pos + Vector2(-1, -1)) #Bot Left
        neighbor_pos.append(current_pos + Vector2(0, -1)) #Bot
        neighbor_pos.append(current_pos + Vector2(1, -1)) #Bot Right
        for node in graph.nodes:
            for pos in neighbor_pos:
                if node.position.x_pos == pos.x_pos and node.position.y_pos == pos.y_pos:
                    neighbors.append(node)
        return neighbors

    def pathfind(self, search):
        '''The A_Star algorithm. Detects a path to a goal node on a grid and returns a path list'''
        goal_found = False
              
        current_node = self.open_list[0]                
        #Adds the starting node to the open_list and sets the current node to the starting node
        while not self.close_list.__contains__(self.goal_node) or len(self.open_list) != 0:
            self.open_list.sort(key = lambda Node: Node.f_score)
            current_node = self.open_list[0] 
            #Sorts the open_list by f_score and adds the lowest to open_list
            self.open_list.remove(current_node)
            self.close_list.append(current_node)
            #Removes the lowest f_score node from open_list and adds it to the close_list
            if self.close_list.__contains__(self.goal_node):
                #Exits the loop if the goal node is added to the close_list
                break
            self.neighbors = self.find_neighbors(search, current_node.position)
            #Finds the neighbor nodes and adds them to a neighbor list
            for neighbor in self.neighbors:
                #if node isn't in open list, and it is not in the closed list, and is traversable  add it, calc g, calc h, clac for
                if not self.close_list.__contains__(neighbor) and neighbor.traversable:
                    self.open_list.append(neighbor)                    
                    neighbor.calc_g(current_node)
                    neighbor.calc_h(self.goal_node)
                    neighbor.calc_f()  
            #Iterates through the neighbor list and calculates the g,h, and f score of all the neighbors
        if self.goal_node not in self.close_list:
            return [] 
        step = self.goal_node                                           
        while step != None:
            self.path.append(step)
            step = step.parent
        #Adds all the parents to a path list and then returns it       
        return self.path

def main():
    start = 23
    goal = 10
    height = 7
    width = 7
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    screen.fill((255, 100, 100))
    pos = Vector2(100, 100)
    pygame.key.set_repeat(1, 1)
    search_area = Graph(Vector2(height, width))
    search_area.create_nodes()
    while True:
        mouse_pos = pygame.mouse.get_pos()
        astar = A_Star(start, goal, search_area)
        path = astar.pathfind(search_area)
        search_area.draw_graph(astar.start_node, astar.goal_node,path, screen, )
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE] != 0:
                return  
            if event.type == pygame.MOUSEBUTTONDOWN():
                 
        pygame.display.update()        
        pygame.display.flip()

main()