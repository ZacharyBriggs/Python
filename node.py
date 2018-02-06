from vector2 import Vector2
class Node:
    def __init__(self, pos):
        self.position = pos
        self.traversable = True
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
        self.parent = None

    def calc_g(self, node):
        if self.position.x_pos is node.position.x_pos or self.position.y_pos is node.position.y_pos:
            self.g_score = node.g_score + 10
        else:
            self.g_score = node.g_score + 14

    def calc_h(self, goal):
        #self.h_score = (abs(goal.position.x_pos - goal.position.y_pos) + abs(self.position.x_pos - self.position.y_pos)) * 10
        self.h_score = self.position.calc_distance(goal) * 10
    def calc_f():
        self.f_score = g_score + h_score

    def set_parent(parent_node):
        self.parent = parent_node
        
    def set_transvers(true):
        self.traversable = False