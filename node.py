'''Node class for making up a graph'''
from vector2 import Vector2
class Node(object):
    '''Node class with functions for calculating g,h, and f score along with functions to modify its properties'''
    
    #Prototype: Node()
    #Description: Creates a node
    #Arguments: A position
    #Precondition: None
    #Postcondition: A node is created
    #Protection: Public.
    def __init__(self, pos, index):
        self.position = pos
        self.index = index
        self.traversable = True
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
        self.parent = None
        self.is_start = False
        self.is_goal = False

    #Prototype: calc_g()
    #Description: Calculates the g_score of the node
    #Arguments: The current node
    #Precondition: A node
    #Postcondition: The node's g_score is set
    #Protection: Public.
    def calc_g(self, current_node):
        '''Calculates the G score of a node'''        
        tentative_g = self.g_score
        if self.position.x_pos is current_node.position.x_pos and self.position.y_pos is current_node.position.y_pos:
            return
        if self.position.x_pos is current_node.position.x_pos or self.position.y_pos is current_node.position.y_pos:            
            tentative_g = current_node.g_score + 10
        else:            
            tentative_g = current_node.g_score + 14
        if current_node.parent != None:
            if tentative_g < self.g_score:
                self.g_score = tentative_g
                self.set_parent(current_node)
                return 
        self.g_score = tentative_g
        self.set_parent(current_node)

    #Prototype: calc_h()
    #Description: Calculates the h_score of the node
    #Arguments: The current node
    #Precondition: A node
    #Postcondition: The node's h_score is set
    #Protection: Public.
    def calc_h(self, goal):
        '''Calculates the H score of a node'''
        self.h_score = self.position.calc_distance(goal.position) * 10

    #Prototype: calc_f()
    #Description: Calculates the f_score of the node
    #Arguments: The current node
    #Precondition: A node
    #Postcondition: The node's f_score is set
    #Protection: Public.
    def calc_f(self):
        '''Calculates the F score of a node'''
        self.f_score = self.g_score + self.h_score

    #Prototype: set_parent()
    #Description: Sets the node's parent to the node passed in
    #Arguments: The parent node
    #Precondition: A node
    #Postcondition: The node's parent is set to the node passed in
    #Protection: Public.
    def set_parent(self, parent_node):
        '''Sets the node's parent to the node passed in'''
        self.parent = parent_node
    
    #Prototype: toggle_traversable()
    #Description: Sets the node's traversable to true if traversable is false and vice versa
    #Arguments: None
    #Precondition: A node
    #Postcondition: The node's traversable is now set to the opposite
    #Protection: Public.
    def toggle_traversable(self):
        '''Changes traversable to false if it is true and vice versa'''
        if self.traversable == True:
            self.traversable = False
        else:
            self.traversable = True
