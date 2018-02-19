from vector2 import Vector2
from node import Node
from graph import Graph
class A_Star:
    def __init__(self, start, goal):
        self.open_list = []
        self.close_list = []  
        self.start_node = start
        self.goal_node = goal
        #Start Node variable
        #search space variable
def find_neighbors(graph, current_pos):
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
                neighbors.append(node) #Don't create a new node you pass in the node at that position
    return neighbors[]

def main():
    #needs to be in a function in the A_Star class
    #startup()
    graph_x = 5
    graph_y = 5
    search_area = Graph(Vector2(graph_x, graph_y))
    search_area.create_nodes()
    current_node = search_area.nodes[6]
    open_list = []
    close_list = []
    goal_node = Vector2(3,3)
    goal_found = False
    while(goal_found == False):
        open_list.append(current_node)
        open_list.remove(current_node)
        close_list.append(current_node)
        open_list = find_neighbors(search_area, current_node.position)
        for item in open_list: #Iterate using the list, This will go out of range and get no existing items    
            item.calc_g(current_node)
            item.calc_h(goal_node)
            item.calc_f()
        open_list.sort(key = lambda Node: Node.f_score)
        current_node = open_list[0]
        for node in open_list:
            open_list.remove(node)
        if close_list[len(close_list) - 1].position == goal_node:
            goal_found = True
main()