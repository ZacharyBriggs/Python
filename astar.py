'''The A_Star pathfinding class'''
from vector2 import Vector2
from node import Node
from graph import Graph
class A_Star:
    def __init__(self, width, height):
        '''Initilizes the A_Star class and creates an open_list, close_list, sets the start_node, and goal_node'''
        self.open_list = []
        self.close_list = []  
        self.search_area = Graph(Vector2(width, height))
        self.search_area.create_nodes()
        self.neighbors = []
        self.path = []
        self.start_node = search.nodes[start]
        self.goal_node = search.nodes[goal]
        self.goal_node.is_goal = True

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

    def pathfind(self, start, goal, search):
        '''The A_Star algorithm. Detects a path to a goal node on a grid and returns a path list'''
        
        step = goal_node
        goal_found = False
        self.open_list.append(search.nodes[start])
        start_node = search.nodes[start]
        start_node.is_start = True
        current_node = self.open_list[0]                
        #Adds the starting node to the open_list and sets the current node to the starting node
        while not self.close_list.__contains__(goal_node) or len(self.open_list) != 0:
            self.open_list.sort(key = lambda Node: Node.f_score)
            current_node = self.open_list[0] 
            #Sorts the open_list by f_score and adds the lowest to open_list
            self.open_list.remove(current_node)
            self.close_list.append(current_node)
            #Removes the lowest f_score node from open_list and adds it to the close_list
            if self.close_list.__contains__(goal_node):
                #Exits the loop if the goal node is added to the close_list
                break
            self.neighbors = self.find_neighbors(search, current_node.position)
            #Finds the neighbor nodes and adds them to a neighbor list
            for neighbor in self.neighbors:
                #if node isn't in open list, and it is not in the closed list, and is traversable  add it, calc g, calc h, clac for
                if not self.close_list.__contains__(neighbor) and neighbor.traversable:
                    self.open_list.append(neighbor)                    
                    neighbor.calc_g(current_node)
                    neighbor.calc_h(goal_node)
                    neighbor.calc_f()  
            #Iterates through the neighbor list and calculates the g,h, and f score of all the neighbors
        if goal_node not in self.close_list:
            return [] 
        step = goal_node                                           
        while step != None:
            self.path.append(step)
            step = step.parent
        #Adds all the parents to a path list and then returns it       
        return self.path

def main():
    astar = A_Star(7, 7)
    path = astar.pathfind(8, 43, astar.search_area)
    astar.search_area.print_graph(astar.start, astar.goal,path)

main()