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
import os
print(os.getcwd())

