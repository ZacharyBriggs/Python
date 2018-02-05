from vector2.py import Vector2
class Node:
    def __init__(self, pos, transversable):
        self.position = pos
        self.is_transversable = transversable
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
        self.parent = None
    def calculate_g(self, node):
        if self.position.x_pos is node.position.x_pos or self.position.y_pos is node.position.y_pos
            self.g_score = node.g_score + 10
        if self.position.x_pos != node.position.x_pos and self.position.y_pos != node.position.y_pos
            self.g_score = node.g_score + 14
    def calculate_h(self, goal):
        self.h_score = (abs(goal.position.x_pos - goal.position.y_pos) + abs(self.position.x_pos - self.position.y_pos)) * 10
    def calculate_f():
        self.f_score = g_score + h_score
    def make_wall()
        self.is_traversable = False