from vector2 import Vector2
from node import Node
from graph import Graph
class A_Star:
    def __init__(self, start, goal):
        self.open_list = []
        self.close_list = []
        self.current_node = start
        self.goal_node = goal
'''def startup(self):
    graph_x = 5
    graph_y = 5
    search_area = Graph(Vector2(graph_x, graph_y))
    search_area.create_nodes()
    current_node = search_area.nodes[6]
    open_list = []
    open_list.append(current_node)
    #search_area.nodes[7].calc_g(search_area.nodes[6])
    #search_area.nodes[7].calc_h(search_area.nodes[18].position)
    #search_area.nodes[7].calc_f()'''
def find_neighbors(graph, current_pos, open_list, goal_node):
    neighbors = []
    neighbor_pos = [] 
    neighbor_pos.append(current_pos + Vector2(-1, 1))
    neighbor_pos.append(current_pos + Vector2(0, 1))
    neighbor_pos.append(current_pos + Vector2(1, 1))
    neighbor_pos.append(current_pos + Vector2(-1, 0))
    neighbor_pos.append(current_pos + Vector2(1, 0))
    neighbor_pos.append(current_pos + Vector2(-1, -1))
    neighbor_pos.append(current_pos + Vector2(0, -1))
    neighbor_pos.append(current_pos + Vector2(1, -1))
    for node in graph.nodes:
        for pos in neighbor_pos:
            if node.position.x_pos == pos.x_pos and node.position.y_pos == pos.y_pos:
                open_list.append(Node(pos, True))

def main():
    #startup()
    graph_x = 5
    graph_y = 5
    a = 0
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
        find_neighbors(search_area, current_node.position, open_list, goal_node)
        for i in range (0,8):
            open_list[i].calc_g(current_node)
            open_list[i].calc_h(goal_node)
            open_list[i].calc_f()
        open_list.sort(key = lambda Node: Node.f_score)
        current_node = open_list[0]
        for node in open_list:
            open_list.remove(node)
        a += 1
            goal_found = True
main()