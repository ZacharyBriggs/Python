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
def find_neighbors( graph, current_pos, open_list):
    neighbors = []
    neighbor_pos = []    
    neightbor_pos.append(current_pos + Vector2(-1, 1))
    neightbor_pos.append(current_pos + Vector2(0, 1))
    neightbor_pos.append(current_pos + Vector2(1, 1))
    neightbor_pos.append(current_pos + Vector2(-1, 0))
    neightbor_pos.append(current_pos + Vector2(1, 0))
    neightbor_pos.append(current_pos + Vector2(-1, -1))
    neightbor_pos.append(current_pos + Vector2(0, -1))
    neightbor_pos.append(current_pos + Vector2(1, -1))
    for node in graph.nodes:
        for pos in neighbor_pos:
            if node.pos == pos:
                neighbors.append(pos)
    return neighbors    

def main():
    #startup()
    graph_x = 5
    graph_y = 5
    search_area = Graph(Vector2(graph_x, graph_y))
    search_area.create_nodes()
    current_node = search_area.nodes[6]
    open_list = []
    close_list = []
    open_list.append(current_node)
    open_list.remove(current_node)
    close_list.append(current_node)
    find_neighbors(search_area, current_node.position, open_list)
    i = 0
main()