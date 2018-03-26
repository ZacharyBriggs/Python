'''Vector2 class and testing'''
#pylint: disable=W0312
import math
class Vector2(object):
	'''Vector 2 class that includes math functions'''
	def __init__(self, xpos, ypos):
		'''Vector 2 initilizer'''
	'''Prototype: Vector2()
	Description: Creates a vector2 with the x position and y position 
	Arguments: The x position and y position
	Precondition: None
	Postcondition: A vector2 is created
	Protection: Public.'''
		self.x_pos = xpos
		self.y_pos = ypos
	
	def __add__(self, other):
		'''Adds two Vec2s together'''
	'''Prototype: +
	Description: A vector2s x is added to the others x and the vector2s y is added to the others y
	Arguments: A vector2
	Precondition: Two vector2s
	Postcondition: The two vector2s are added together
	Protection: Public.'''
		new_vec = Vector2(self.x_pos + other.x_pos, self.y_pos + other.y_pos)
		return new_vec

	def __sub__(self, other):
		'''Subtracts two Vec2s'''
	'''Prototype: -
	Description: A vector2s x is subtracted from the others x and the vector2s y is subtracted from the others y
	Arguments: A vector2
	Precondition: Two vector2s
	Postcondition: The two vector2s are subtracted
	Protection: Public.'''
		new_vec = Vector2(self.x_pos - other.x_pos, self.y_pos - other.y_pos)
		return new_vec

	def __mul__(self, other):
		'''Multiplys the X and Y of a Vec2 by a scaler value'''
	'''Prototype: *
	Description: Multiples a vector2s x and y by a scaler value
	Arguments: A scaler value
	Precondition: A vector2
	Postcondition: The vector2 is multiplyed by the scaler
	Protection: Public.'''
		new_vec = Vector2(self.x_pos * other, self.y_pos * other)
		return new_vec

	def __eq__(self, other):
		'''Compares the x and y of two vectors and returns true/false'''
	'''Prototype: ==
	Description: Compares two vector2s
	Arguments: A vector2
	Precondition: Two vector2s
	Postcondition: The two vector2s are compared and returns the result
	Protection: Public.'''
		return self.x_pos == other.x_pos and self.y_pos == other.y_pos

	def dot(self, other):
		'''Multiplys two Vec2s togther'''
	'''Prototype: *
	Description: A vector2s x is multiplyed by the others x and the vector2s y is multiplyed with the others y
	Arguments: A vector2
	Precondition: Two vector2s
	Postcondition: The two vector2s are multiplyed
	Protection: Public.'''
		temp = self.x_pos*other.x_pos + self.y_pos * other.y_pos
		return temp

	def magnitude(self):
		'''Finds the magnitude of a Vec2'''
		mag = math.sqrt(self.x_pos * self.x_pos + self.y_pos * self.y_pos)
		return mag

	def normalize(self):
		'''Normalizes a Vec2'''
		mag = self.magnitude()
		new_vec = Vector2(self.x_pos / mag, self.y_pos / mag)
		return new_vec

	def calc_distance(self, other):
		'''Calculates the distance between 2 vector2s'''
		return abs(other.x_pos - self.x_pos) + abs(other.y_pos - self.y_pos)