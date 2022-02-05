def times2(number):
	answer = number *2
	return answer
print(times2(2))
all_hope = 'Here be dragons'
def all_your_vars_are_belong_to_us(variables):
	my_variable = 'Make your time'
	print('parameter passed into the function:', variables)
	print('Global variable:', all_hope)
	print('Local variable:', my_variable)
old_meme_is_old = 'Somebody set up us the bomb'
all_your_vars_are_belong_to_us(old_meme_is_old)
print (all_your_vars_are_belong_to_us)
global_int = 0
def inc_it(x):
	global global_int
	x = x +1
	global_int = global_int + 1
	return x
y = 10
print(inc_it(y))
print( y)
def f(n):
	assert n >=0
	answer = 1
	while n > 1:
		answer *= n
		n -= 1
	return answer
print(f(0))



class Person(object):
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
# This type of method is called an accessor (or getter)
    def get_name(self):
    	return self.name
# This type of method is called a mutator
    def set_name(self, name):
    	self.name = name
    def get_age(self):
    	return self.age
    def set_age(self, age):
    	self.age = age
    def get_height(self):
    	return self.height
    def set_height(self, height):
    	self.height = height
    def get_weight(self):
    	return self.weight
    def set_weight(self, weight):
    	self.weight = weight
# Underbar methods have special significance in Python
    def __str__(self):
    	return 'Name:' + self.name + ', Age:' + str(self.age) + ', Height:' + str(self.height) +  ', Weight:' + str(self.weight)
    def __eq__(self, other):
    	return self.name == other.name
mitch = Person('Mitch', 32, 70, 200)
sarina = Person('Sarina', 25, 65, 130)
print (mitch)
print (sarina)
print (type(mitch))
print (type(sarina))



def increment(n):
	return n+1
def square(n):
	return n**2

def apply(opList, arg):
	if len(opList)==0:
		return arg
	else:
		return apply(opList[1:], opList[0](arg))
print(apply([increment], 7))
print(len(([increment], 7)))
print(type(([increment], 7)))
print(apply([square], 7))
print(apply([increment, square], 7))



for i in range(0,10):
	for j in range(10,100):
		print(i,j)
		if j % 2 ==0:
			break
print(i,j)

t = (0.1, 0.3)
x = 0.0
for i in t:
	for j in t:
		x += i + j
		print (i,j,x)
print (i,j)


def f(s):
	if len(s) <= 1:
		return s
	else: 
		return f(f(s[1:])) + s[0]
print (f('mat'))


def intersect(seq1, seq2):
	res = []
	for x in seq1:
		if x in seq2:
			res.append(x)
		else: 
			print ('Hoan is so cute')

	return res

s1 = 'SPAMl'
s2 = 'SCAMq'
print(intersect(s1,s2))




def outer_function(msg):
	message = msg

	def inner_function():
		print(message)
	return inner_function

hi_func = outer_function('hi')
bye_func = outer_function('Bye')

hi_func()
bye_func()


def outer_function(msg):
	def inner_function():
		print(msg)
	return inner_function

def decorator_function(message):
	def wrapper_function():
		print(message)
	return wrapper_function

def original_function():
	print('Hoan is so cute')


def decorator_function(original_function):
	def wrapper_function(*args, **kwargs):
		print('wrapper executed this before: {} '.format(original_function.__name__))
		return original_function(*args, **kwargs)

	return wrapper_function
decorator_function(original_function)()

def display():
	print('display function ran')

decorated_display = decorator_function(display)
decorated_display()

@decorator_function
def display_info(name, age):
	print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)


class decorator_class(object):
	def __init__(self, original_function):
		self.original_function = original_function



	def __call__(self, *args, **kwargs):
		print('call method executed this before: {} '.format(self.original_function.__name__))
		return self.original_function(*args, **kwargs)

@decorator_class
def display():
	print('display function ran')
@decorator_class
def display_info(name, age):
	print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)
display()






















