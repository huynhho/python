class  Employee:
	def __init__(self, first, last):
		self.first = first
		self.last = last


	@property	
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last

	@fullname.deleter 
	def fullname(self):
		print('Delete Name!')
		self.first = None
		self.last = None

	def 






	@property
	def email(self):
		return '{}.{}@email.com'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')

emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname







# Python OOp Tutorial 6: Property Decorators-Getters, Setters, and Deleters
class  Human():
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender

	def speak_name(self):
		print ('My name is %s' % self.name)

	def speak(self, text):
		print (text)

	def perform_math_task(self, math_operation, *args):
		print("{} performed a math operation and the result was {}".format(self.name, math_operation(*args)))

def add(a,b,c):
	return a + b +c
ryan = Human("Ryan Stevens", "Male")
ryan.perform_math_task(add, 40, 50,60)


class Rectangle():
	def __init__(self, width, length):
		self.width = width
		self.length = length

	def area(self):
		return self.width * self.length

	def perimeter(self):
		return (self.length  + self.width) * 2
rectangle = Rectangle(5, 10)
print(rectangle.area())
print(rectangle.perimeter())


class Employee: # Common base class for all employees

	empCount = 0
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount +=1
	def displayCount(self):
		print('Total Employee %d' % Employee.empCount)
	def displayEmployee(self):
		print('Name: ', self.name, 'Salary: ', self.salary)
hoan = Employee('hoan',10000)
han = Employee('han', 50000)
luc = Employee('luc', 6000)
print(hoan.name)
hoan.displayEmployee()
han.displayCount()
print(Employee.empCount)

print(hasattr(hoan, 'salary'))

setattr(hoan, 'age', 8)
print(hoan.age)
print(getattr(hoan, 'age'))


class Tree:
	def __init__(self, left, right):
		self.left = left
		self.right = right
t = Tree(Tree('a', 'b'), Tree('c', 'd'))
print(t.left.right)
print(t.left)

class Node:
	def __init__(self, value, next = None):
		self.value = value
		self.next = next
L = Node('a', Node('b', Node('c', Node('d'))))
print(L.next.next.next.value)


class FirstClass:
	def setdata(self, value):
		self.data = value
	def display(self):
		print(self.data)
x = FirstClass()
y = FirstClass()
print(x.setdata('King Arthur'))
y.setdata(3.14159)


