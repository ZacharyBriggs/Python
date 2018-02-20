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
        self.open_list.append(self.search_area.nodes[18])
        self.parents = []
        self.neighbors = []

    def pathfind(self):
        goal_found = False
        #add starting node to open_list
        while(goal_found == False):
            #find lowest f score in open_list
            self.open_list.sort(key = lambda Node: Node.f_score) 
            current_node = self.open_list[0]
            self.open_list.append(current_node) 
            #Move lowest f score to closed list and remove it from the open list
            self.open_list.remove(current_node)
            self.close_list.append(current_node)
            #find node neighbors
            self.neighbors = self.search_area.find_neighbors(current_node.position)
            for neighbor in self.neighbors:
                #if node isn't in open list, and it is not in the closed list, and is traversable  add it, calc g, calc h, clac for
                
                if self.close_list.__contains__(neighbor):
                    continue
                else:
                    self.open_list.append(neighbor)
                for item in self.open_list:
                    if item.traversable:
                item.calc_g(current_node)
                item.calc_h(self.goal_node)
                item.calc_f()
                if item.g_score < current_node.g_score:
                    current_node = item
                #if node is in open list or has a parent
                    #calculate a tentative g and if the tentative g is better than the nodes current g
                    #reparent the node and set the g to the tentative and recalc f score
            #stop once
                #goal node is in the closed list
                #open list is empty
            if self.close_list[len(self.close_list) - 1].position == self.goal_node:
                goal_found = True
                self.parents.append(current_node)
                break
            
            item.set_parent(current_node)
            self.parents.append(current_node)

def main():
    astar = A_Star(Vector2(0, 0),Vector2(6, 4))
    astar.startup(7, 7)
    astar.pathfind()
main()