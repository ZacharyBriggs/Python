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
        search_area = Graph(Vector2(width, height))
        search_area.create_nodes()
        open_list = []
        open_list.append(search_area.nodes[6])
        close_list = []
        parents = []
        neighbors = []
        goal_node = Vector2(3,3)

    def pathfind(self):
        goal_found = False
        while(goal_found == False):
            current_node = open_list[0]
            open_list.append(current_node)
            close_list.append(current_node)
            if close_list[len(close_list) - 1].position == goal_node:
                goal_found = True
                break
            neighbors = find_neighbors(search_area, current_node.position)
            for neighbor in neighbors:
                open_list.append(neighbor)
            for item in open_list:
                if item.traversable == True:
                    item.calc_g(current_node)
                    #if item.parent != None:
                        #if item.g_score < item.parent.g_score:
                            #item.parent = item
                    item.calc_h(goal_node)
                    item.calc_f()
                    if item.g_score < current_node.g_score:
                        current_node = item
                item.set_parent(current_node)
        parents.append(current_node)
        open_list.sort(key = lambda Node: Node.f_score)

def find_neighbors(self, graph, current_pos):
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

def main():
    astar = A_Star(Vector2(1,1),Vector2(3,3))
    astar.startup(5,5)
    astar.pathfind()
main()