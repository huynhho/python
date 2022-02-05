### Add record field initialization
##class Person:
##    def__init__(self, name, job, pay):
##        self.name = name # Constructor takes three arguments
##        self.job = job   # Fill out fields when created
##        self.pay = pay   # self is the new instance object
# Add incremental self-test code
##class Person:
##    def__init__(self, name, job=None, pay =0):
##        self.name = name
##        self.job = job
##        self.pay = pay
##
##bob = Person('Bob Smith')
##sue = Person('Sue Jones', job='dev', pay = 100000)
##print(bob.name, bob.pay)
##print(sue.name, sue.pay)
##
##class Staff601:
##    course = "6.01"
##    building = 34
##    room = 501
##print(Staff601.room)
##class Staff601:
##    def salutation(self):
##        return self.role + ' ' + self.name
##    course = 'learn about Hoan'
##    building = 34
##    room = 501
##    
class Staff601:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary
    def salutation(self):
        return self.role + ' ' + self.name
    def giveRaise(self, percentage):
        self.salary = self.salary + self.salary * percentage

# to create an instance
pat = Staff601('Pat', 'Professor', 100000)







def value(self, t, v0=None):
	if v0 is not None:
		self.v0 = v0
	g = 9.81
	try:
		value = self.v0*t - 0.5*g*t**2
	except AttributeError:
		msg =  'You cannot call value(t) without first calling value(t, v0) to set v0'
		raise TypeError(msg)
	return value



import time
class Time():
	pass

#print(time.hours)
#print(time.minutes)

def addTime(t1, t2):
	sum = Time()
	sum.hours = t1.hours + t2.hours
	sum.minutes = t1.minutes + t2.minutes
	sum.seconds = t1.seconds + t2.seconds
	return sum

currentTime = Time()
currentTime.hours = 9
currentTime.minutes = 14
currentTime.seconds = 30

breadTime = Time()
breadTime.hours = 3
breadTime.minutes = 35
breadTime.seconds = 0

doneTime = addTime(currentTime, breadTime)


class Customer(object):
	def __init__(self, name, balance = 0.0):
		self.name = name
		self.balance = balance
	def withdraw(self, amount):
		if amount > self.balance:
			raise RuntimeError('Amount greater than available balance.')
		self.balance -= amount
		return self.balance
	def deposit(self, amount):
		self.balance += amount
		return self.balance


print(sum)
sum = 500
print(sum)
def myfunc(n):
    sum = n + 1
    #print (sum)
    return sum
print(myfunc(2))
sum = myfunc(2) + 1
print(sum)

a = 20; b = -2.5 # global variables
def f1(x):
    a = 21 # this is a new local variable
    return a*x + b # 21*x -2.5
print(a)   # yields 20

def f2(x):
    global a
    a = 21 # the global a is changed
    return  a*x + b # 21*x -2.5
print(a)
print(f1(100))
print(f2(1000))
print(a)


def makelist(start, stop, inc):
	value = start
	result = []
	while value <= stop:
		result.append(value)
		value = value + inc
	return result
mylist = makelist(0, 100,20)
print(mylist)