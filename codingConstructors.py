class Y:
	"""The vertical motion of a ball."""
	def __init__(self, v0):
		self.v0 = v0
		self.g = 9.81
	def value(self, t):
		return  self.v0*t - 0.5*self.g*t**2
	def formula(self):
		return ('v0*t - 0.5*g*t**2; v0=%g' % self.v0)

y = Y(5)
t = 0.2
v = y.value(t)
#print('y(t={}; v0={}) = {}'.format(t, y.v0, v))
#print(y.formula())


class VelocityProfile:
	def __init__(self, beta, mu0, n, R):
		self.beta = beta
		self.mu0 = mu0
		self.n = n
		self.R = R
	def value(self, r):
		beta, mu0, n, R = self.beta, self.mu0, self.n, self.R
		v = (beta/(2.0*mu0))**(1/n)*(n/(n+1))*(R**(1+1/n)- r**(1+1/n))
		return v

class Y2:
	def value(self, t, v0=None):
		if v0 is not None:
			self.v0 = v0
		if not hasattr(self, 'v0'):
			print('You cannot call value(t) without first calling value(t,v0) to set v0')
			return None
		g = 9.81
		return self.v0*t - 0.5*g*t**2
hoan = Y2()
#print(hoan.value(0.2))

class Account:
	def __init__(self, name, account_number, initial_amount):
		self.name = name
		self.no = account_number
		self.balance = initial_amount
	def deposit(self, amount):
		self.balance +=  amount
	def withdraw(self, amount):
		self.balance -= amount
	def dump(self):
		s = '{}, {}, balance: {}'.format(self.name, self.no, self.balance)
		print (s)

a1 = Account('John 01sson', '19371554951', 20000)
a2 = Account('Liz 01sson', '111111111111', 122222)
a1.deposit(1000)
a2.withdraw(12222)
print(a1.dump())
print(a2.dump())