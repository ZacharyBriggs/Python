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
        self.open_list.append(self.search_area.nodes[6])
        self.parents = []
        self.neighbors = []

    def pathfind(self):
        goal_found = False
        while(goal_found == False):
            current_node = self.open_list[0]
            self.open_list.append(current_node)
            self.close_list.append(current_node)
            if self.close_list[len(self.close_list) - 1].position == self.goal_node:
                goal_found = True
                break
            self.neighbors = self.search_area.find_neighbors(current_node.position)
            for neighbor in self.neighbors:
                self.open_list.append(neighbor)
            for item in self.open_list:
                if item.traversable == True:
                    item.calc_g(current_node)
                    #if item.parent != None:
                        #if item.g_score < item.parent.g_score:
                            #item.parent = item
                    item.calc_h(self.goal_node)
                    item.calc_f()
                    if item.g_score < current_node.g_score:
                        current_node = item
                item.set_parent(current_node)
            self.parents.append(current_node)
            self.open_list.sort(key = lambda Node: Node.f_score)

def main():
    astar = A_Star(Vector2(2, 4),Vector2(6, 4))
    astar.startup(7, 7)
    astar.pathfind()
main()