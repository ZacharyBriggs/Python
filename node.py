'''Node class for making up a graph'''
from vector2 import Vector2
class Node(object):
    def __init__(self, pos):
        self.position = pos
        self.traversable = True
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
        self.parent = None

    def calc_g(self, current_node):
        '''Calculates the G score of a node'''
        #if node is in open list or has a parent
        #calculate a tentative g and if the tentative g is better than the nodes current g
        #reparent the node and set the g to the tentative and recalc f score  
        tentative_g = self.g_score
        if self.position.x_pos is current_node.position.x_pos and self.position.y_pos is current_node.position.y_pos:
            return
        if self.position.x_pos is current_node.position.x_pos or self.position.y_pos is current_node.position.y_pos:
            self.g_score = current_node.g_score + 10
            tentative_g = current_node.g_score + 10
            if tentative_g < self.g_score:
                self.g_score = tentative_g
        else:
            self.g_score = current_node.g_score + 14
            tentative_g = current_node.g_score + 14
            if tentative_g < self.g_score:
                self.g_score = tentative_g   
         self.set_parent(current_node)

    def calc_h(self, goal):
        '''Calculates the H score of a node'''
        self.h_score = self.position.calc_distance(goal.position) * 10

    def calc_f(self):
        '''Calculates the F score of a node'''
        self.f_score = self.g_score + self.h_score

    def set_parent(self, parent_node):
        '''Sets the node's parent to the node passed in'''
        self.parent = parent_node
        
    def toggle_traversable():
        '''Changes traversable to fale if it is true and vice versa'''
        if self.traversable == True:
            self.traversable = False
        else:
            self.traversable = True