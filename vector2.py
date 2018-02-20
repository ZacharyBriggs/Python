'''Vector2 class and testing'''
#pylint: disable=W0312
import math
class Vector2(object):
	'''Vector 2 class that includes math functions'''
	def __init__(self, xpos, ypos):
    	'''Vector 2 initilizer'''
		self.x_pos = xpos
		self.y_pos = ypos
	
	def __add__(self, other):
		'''Adds two Vec2s together'''
		new_vec = Vector2(self.x_pos + other.x_pos, self.y_pos + other.y_pos)
		return new_vec

	def __sub__(self, other):
    	'''Subtracts two Vec2s'''
		new_vec = Vector2(self.x_pos - other.x_pos, self.y_pos - other.y_pos)
		return new_vec

	def __mul__(self, other):
    	'''Multiplys the X and Y of a Vec2 by a scaler value'''
		new_vec = Vector2(self.x_pos * other, self.y_pos * other)
		return new_vec

	def __eq__(self, other):
    	'''Compares the x and y of two vectors and returns true/false'''
		return self.x_pos == other.x_pos and self.y_pos == other.y_pos

	def dot(self, other):
    	'''Multiplys two Vec2s togther'''
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