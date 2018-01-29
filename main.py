def add(lhs,rhs):
	return lhs+rhs
def subtract(lhs,rhs):
	return lhs-rhs
def multiply(lhs,rhs):
	return lhs*rhs
def divide(lhs,rhs):
	return lhs/rhs
y=True
n=False
end = y
while end != n:
	num_a,num_b = input("Input two numbers. ")
	operator = input("Choose an operator to perform on the numbers. Addition = 0, Subtraction = 1, \nMultiplication = 2, Division = 3. ")
	if operator is 0:
		print add(num_a,num_b)
	elif operator is 1:
		print subtract(num_a,num_b)
	elif operator is 2:
		print multiply(num_a,num_b)
	elif operator is 3:
		print divide(num_a,num_b)
	end = input("Would you like to perform another operation?")