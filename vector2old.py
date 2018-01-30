import math
def add(lhs,rhs):
	temp = [lhs[0]+rhs[0],lhs[1]+rhs[1]]
	return temp
def subtract(lhs,rhs):
	temp = [lhs[0]-rhs[0],lhs[1]-rhs[1]]
	return temp
def multiply(lhs,rhs):
	temp = [lhs[0]*rhs[0],lhs[1]*rhs[1]]
	return temp
def scale(list,scaler):
	temp = [list[0]*scaler,list[1]*scaler]
	return temp
def divide(lhs,rhs):
	temp = [lhs[0]/rhs[0],lhs[1]/rhs[1]]
	return temp
def magnitude(vector):
	mag = math.sqrt(vector[0]*vector[0]+vector[1]*vector[1])
	return mag
def normalize(vector):
	mag = magnitude(vector)
	temp = [vector[0]/mag,vector[1]/mag]
	return temp
list_one = [5,7]
list_two = [1,10]
print add(list_one,list_two)
print subtract(list_one,list_two)
print multiply(list_one,list_two)
print scale(list_two,2)
print divide(list_one,list_two)
print normalize(list_one)