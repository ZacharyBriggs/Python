'''The A_Star pathfinding class'''
from vector2 import Vector2
from node import Node
from graph import Graph
class A_Star:
    def __init__(self, start, goal):
        '''Initilizes the A_Star class and creates an open_list, close_list, sets the start_node, and goal_node'''
        self.open_list = []
        self.close_list = []  
        self.start_node = start
        self.goal_node = goal

    def startup(self, width, height):
        '''Creates the graph, sets the goal_node, and creates the neighbors list'''
        self.search_area = Graph(Vector2(width, height))
        self.search_area.create_nodes()
        self.goal_node = self.search_area.nodes[self.goal_node]
        self.goal_node.is_goal = True 
        self.neighbors = []

    def pathfind(self):
        '''The A_Star algorithm. Detects a path to a goal node on a grid and returns a path list'''
        goal_found = False
        self.open_list.append(self.search_area.nodes[self.start_node])
        self.start_node = self.search_area.nodes[self.start_node]
        self.start_node.is_start = True
        current_node = self.open_list[0]
        #Adds the starting node to the open_list and sets the current node to the starting node
        while not self.close_list.__contains__(self.goal_node) or len(self.open_list) == 0:
            self.open_list.sort(key = lambda Node: Node.f_score)
            current_node = self.open_list[0] 
            #Sorts the open_list by f_score and adds the lowest to open_list
            self.open_list.remove(current_node)
            self.close_list.append(current_node)
            #Removes the lowest f_score node from open_list and adds it to the close_list
            if self.close_list.__contains__(self.goal_node):
                #Exits the loop if the goal node is added to the close_list
                break
            self.neighbors = self.search_area.find_neighbors(current_node.position)
            #Finds the neighbor nodes and adds them to a neighbor list
            for neighbor in self.neighbors:
                #if node isn't in open list, and it is not in the closed list, and is traversable  add it, calc g, calc h, clac for
                if not self.close_list.__contains__(neighbor) and neighbor.traversable:
                    self.open_list.append(neighbor)                    
                    neighbor.calc_g(current_node)
                    neighbor.calc_h(self.goal_node)
                    neighbor.calc_f()  
            #Iterates through the neighbor list and calculates the g,h, and f score of all the neighbors                                            
        path = []
        step = self.goal_node
        path.append(step)
        while step.parent != None:
            path.append(step.parent)
            step = step.parent
        #Adds all the parents to a path list and then returns it       
        return path

def main():
    astar = A_Star(8, 46)
    astar.startup(7, 7)
    path = astar.pathfind()
    astar.search_area.print_graph(astar.start_node, astar.goal_node,path)
    b = 0

main()