from vector2 import Vector2
class Node:
    def __init__(self, pos, traversable):
        self.position = pos
        self.traversable = traversable
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
        self.parent = None

    def calc_g(self, current_node):
        if self.position.x_pos is current_node.position.x_pos or self.position.y_pos is current_node.position.y_pos:
            self.g_score = current_node.g_score + 10
        else:
            self.g_score = current_node.g_score + 14

    def calc_h(self, goal):
        self.h_score = self.position.calc_distance(goal) * 10

    def calc_f(self):
        self.f_score = self.g_score + self.h_score

    def set_parent(parent_node):
        self.parent = parent_node
        
    def set_transvers(true_false):
        self.traversable = true_false