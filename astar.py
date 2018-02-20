from vector2 import Vector2
from node import Node
from graph import Graph
class A_Star:
    def __init__(self, start, goal):
        self.open_list = []
        self.close_list = []  
        self.start_node = start
        self.goal_node = goal
        #search space variable

    def startup(self, width, height):
        self.search_area = Graph(Vector2(width, height))
        self.search_area.create_nodes()
        self.open_list.append(self.search_area.nodes[self.start_node])
        self.goal_node = self.search_area.nodes[self.goal_node] 
        self.neighbors = []

    def pathfind(self):
        goal_found = False
        current_node = self.open_list[0]
        #add starting node to open_list
        while not self.close_list.__contains__(self.goal_node) or len(self.open_list) == 0:
            #find lowest f score in open_list
            self.open_list.sort(key = lambda Node: Node.f_score)
            current_node = self.open_list[0] 
            #Move lowest f score to closed list and remove it from the open list
            self.open_list.remove(current_node)
            self.close_list.append(current_node)
            if self.close_list.__contains__(self.goal_node):
                break
            #find node neighbors
            self.neighbors = self.search_area.find_neighbors(current_node.position)
            for neighbor in self.neighbors:
                #if node isn't in open list, and it is not in the closed list, and is traversable  add it, calc g, calc h, clac for
                if not self.close_list.__contains__(neighbor) and neighbor.traversable:
                    self.open_list.append(neighbor)                    
                    neighbor.calc_g(current_node)
                    neighbor.calc_h(self.goal_node)
                    neighbor.calc_f()    
                                                              
            #stop once
                #goal node is in the closed list
                #open list is empty
        path = []
        step = self.goal_node
        path.append(step)
        while step.parent != None:
            path.append(step.parent)
            step = step.parent        
        return path
def main():
    astar = A_Star(18, 46)
    astar.startup(7, 7)
    a = astar.pathfind()
    b = 0

main()