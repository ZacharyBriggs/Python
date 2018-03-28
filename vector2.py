'''Vector2 class and testing'''
#pylint: disable=W0312
import math
class Vector2(object):
	'''Vector 2 class that includes math functions'''

	#Prototype: Vector2()
	#Description: Creates a vector2 with the x position and y position 
	#Arguments: The x position and y position
	#Precondition: None
	#Postcondition: A vector2 is created
	#Protection: Public.
	def __init__(self, xpos, ypos):
    		'''Vector 2 initilizer'''
		self.x_pos = xpos
		self.y_pos = ypos
	
	#Prototype: +
	#Description: A vector2s x is added to the others x and the vector2s y is added to the others y
	#Arguments: A vector2
	#Precondition: Two vector2s
	#Postcondition: The two vector2s are added together
	#Protection: Public.
	def __add__(self, other):
		'''Adds two Vec2s together'''
		new_vec = Vector2(self.x_pos + other.x_pos, self.y_pos + other.y_pos)
		return new_vec

	#Prototype: -
	#Description: A vector2s x is subtracted from the others x and the vector2s y is subtracted from the others y
	#Arguments: A vector2
	#Precondition: Two vector2s
	#Postcondition: The two vector2s are subtracted
	#Protection: Public.
	def __sub__(self, other):
		'''Subtracts two Vec2s'''
		new_vec = Vector2(self.x_pos - other.x_pos, self.y_pos - other.y_pos)
		return new_vec

	#Prototype: *
	#Description: Multiples a vector2s x and y by a scaler value
	#Arguments: A scaler value
	#Precondition: A vector2
	#Postcondition: The vector2 is multiplyed by the scaler
	#Protection: Public.
	def __mul__(self, other):
		'''Multiplys the X and Y of a Vec2 by a scaler value'''
		new_vec = Vector2(self.x_pos * other, self.y_pos * other)
		return new_vec

	#Prototype: ==
	#Description: Compares two vector2s
	#Arguments: A vector2
	#Precondition: Two vector2s
	#Postcondition: The two vector2s are compared and returns the result
	#Protection: Public.
	def __eq__(self, other):
		'''Compares the x and y of two vectors and returns true/false'''	
		return self.x_pos == other.x_pos and self.y_pos == other.y_pos

	#Prototype: *
	#Description: A vector2s x is multiplyed by the others x and the vector2s y is multiplyed with the others y
	#Arguments: A vector2
	#Precondition: Two vector2s
	#Postcondition: The two vector2s are multiplyed
	#Protection: Public.
	def dot(self, other):
		'''Multiplys two Vec2s togther'''	
		temp = self.x_pos*other.x_pos + self.y_pos * other.y_pos
		return temp

	#Prototype: magnitude()
	#Description: Multplies the square root of one vector2s x with its own x and its y with its y 
	#Arguments: None
	#Precondition: A vector2
	#Postcondition: The magnitude of the vector2 is returned
	#Protection: Public.
	def magnitude(self):
		'''Finds the magnitude of a Vec2'''
		mag = math.sqrt(self.x_pos * self.x_pos + self.y_pos * self.y_pos)
		return mag

	#Prototype: normalize()
	#Description: Finds a vector2s magnitude and then normalizes the vector2 by dividing the x and y by the vector2s magnitude 
	#Arguments: None
	#Precondition: A vector2
	#Postcondition: A vector2 is created
	#Protection: Public.
	def normalize(self):
		'''Normalizes a Vec2'''
		mag = self.magnitude()
		new_vec = Vector2(self.x_pos / mag, self.y_pos / mag)
		return new_vec

	#Prototype: calc_distance()
	#Description: Calculates the distance between two vector2s
	#Arguments: A vector2
	#Precondition: Two vector2s
	#Postcondition: Returns the absolute value distance
	#Protection: Public.
	def calc_distance(self, other):
		'''Calculates the distance between 2 vector2s'''
		return abs(other.x_pos - self.x_pos) + abs(other.y_pos - self.y_pos)