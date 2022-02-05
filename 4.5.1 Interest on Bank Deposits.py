def improve(update, close, guess=1):
	while not close(guess):
		guess = update(guess)
	return guess
def golden_update(guess):
	return 1/guess + 1
def square_close_to_successor(guess):
	return approx_eq(guess*guess, guess + 1)
def approx_eq(x, y, tolerance=1e-3):
	return abs(x-y) < tolerance
phi = improve(golden_update, square_close_to_successor)
#print(phi)
from math import pi, sqrt

def area(x,y):
	assert x > 0, 'A length must be positive'
	return x*x*y

def area_square(x):
	return area(x,1)

def area_circle(x):
	return area(x,pi)

def area_hexagon(x):
	return area(x,3*sqrt(3)/2)

#print(area_hexagon(4))
#assert 3<=3, 'Math is broken'

def fib(n):
	"""Compute the nth Fibonacci number, for N>=1."""
	assert n > 0, 'n must be greater than 0' # Hoan created this line
	pred, curr = 0, 1
	k = 1
	while k < n:
		pred, curr = curr, pred + curr # The next Fibonacci number is the sum of the current one and  its predecessor
		k = k + 1
	return curr

#print(fib(3))
# Is this alternative definition of fib the same or different from the original fib?
def fib2(n):
	pred, curr = 1, 0
	k = 0 
	while k < n:
		pred, curr = curr, pred + curr
		k = k + 1
	return curr
#print(fib2(3))


#61A Fall 2013 Lecture 15 Video 4


class Account:
	"""An account has a balance and a holder
	>>>a = Account('John')
	>>>a.deposit(100)
	100
	>>>a.withdraw(90)
	10
	>>>a.withdraw(90)
	'Insufficient funds'
	>>>a.balance
	10
	"""
	def __init__(self, account_holder):
		self.balance = 0
		self.holder = account_holder

	def deposit(self, amount):
		"""Add amount to balance."""
		self.balance = self.balance + amount
		return self.balance
	def withdraw(self, amount):
		"""Subtract amount from balance if funds are available"""
		if amount > self.balance:
			print("Insufficient funds")
			return "Insufficient funds"
		self.balance = self.balance - amount
		return self.balance

print(Account)
john = Account('John')
print(john)
john.balance
john.deposit(30)
john.deposit(40)
john.withdraw(70)
# print("Withdraw(70):",john.withdraw(33))
# print(getattr(john, 'balance'))
# print(getattr)
# print(hasattr)
# print(hasattr(john, 'balance'))
# print(hasattr(john, 'expert'))
# print(Account.deposit)
# print(Account.withdraw)
# print(john.deposit)
#assert False, "Evaluate the gap between the target and the reach"
#print(type(TypeError))
#print(TypeError('Bad argument!'))
#raise TypeError("It's how slow you can do it correctly")
# def invert(x):
# 	y = 1/x
# 	print('Never printed if x is 0')
# 	return y 

# def invert_safe(x):
# 	try:
# 		return invert(x)
# 	except ZeroDivisionError as e:
# 		print('handled', e)
# 		return 0

# print(invert_safe(2))
# print(invert_safe(3))	
# print(invert_safe(0))

# How will the Python interpreter respond?
def invert(x):
	result = 1/x  # Raises a ZeroDivisionError if x is 0
	print('Never printed if x is 0')
	return result
def invert_safe(x):
	try:
		return invert(x)
	except ZeroDivisionError as e:
		return str(e)

class Retriever:
	def __lt__(dog1, dog2):
		return dog1.age < dog2.age