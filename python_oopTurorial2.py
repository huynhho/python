class Employee:
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@gmail.com'
		
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = self.pay   +  2

emp_1 = Employee('Hoan', 'Huynh', 50000)
emp_2 = Employee('Test','User', 60000)


print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)



# Python Object_Oriented Programming


class Employee:
	
	raise_amount = 1.04
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@gmail.com'
		#self.fullname = first +  ' ' + last
		#self.appy_raise = pay * 1.04
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay  * self.raise_amount)

emp_1 = Employee('Hoan', 'Huynh', 50000)
emp_2 = Employee('Test','User', 60000)


print(emp_1.pay)
print(emp_1.apply_raise())
print(emp_1.pay)
print(emp_2.apply_raise())
print(emp_2.pay)
print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employee.__dict__)
