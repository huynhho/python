# c = input('c=? ')
# c = float(c)
# F = (9/5)*c +32
# print(F)
# from django.db import models

# class Reporter(models.Model):
# 	first_name = models.CharField(max_length=30)
# 	last_name = models.CharField(max_length=30)
# 	email = models.EmailField()

# 	def __str__(self):
# 		return "%s %s" % (self.first_name, self.last_name)

# from datetime import date
# print(date.today())
# #print(a)
# #assert False, "Error"
# assert True
# print(__debug__)
# def newton_update(f, df):
# 	def update(x):
# 		return x - f(x)/ df(x)
# 	return update
# class IterImproveError(Exception):
# 	def __init__(self, last_guess):
# 		self.last_guess = last_guess

# def improve(update, done, guess=1, max_updates=1000):
# 	k = 0
# 	try:
# 		while not done(guess) and k < max_updates:
# 			guess = update(guess)
# 			k = k + 1
# 		return guess
# 	except ValueError:
# 		raise IterImproveError(guess)
# def find_zero(f, quess=1):
# 	def done(x):
# 		return f(x) == 0
# 	try:
# 		return improve(newton_update(f), done, guess)
# 	except IterImproveError as e:
# 		return e.last_guess
# from math import sqrt
# print(find_zero(lambda x: 2*x*x + sqrt(x)))


#   61A Fall 2016 Lecture 29 Video 6

def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result
my_nums = square_numbers([1,2,3,4,5])
for num in my_nums:
	print(num)
#print(my_nums)


def square_numbers(nums):
    for i in nums:
        yield ( i*i )
my_nums = square_numbers([1,2,3,4,5])
#print(my_nums)
#print(next(my_nums))
class Countdown:
	def __init__(self, start):
		self.start = start

	def __iter__(self):
		v = self.start
		while v > 0:
			yield v
			v -= 1
print(Countdown(8))
a = list(Countdown(5))
print(a)			