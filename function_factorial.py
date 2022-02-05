Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #def fact(n): def f(n): assert n >= 0
assert n >= 0 if n <= 1:
answer = 1 return n
while n > 1: else:
answer *= n return n*fact(n - 1)
SyntaxError: invalid syntax
>>> def fact(n):
	assert n>=0
	if n<=1:
		return n
	else:
		return n*fact(n-1)

	
>>> fact(2)
2
>>> fact(3)
6
>>> fact(4)
24
>>> fact(5)
120
>>> fact(6)
720
>>> fact(7)
5040
>>> fact(8)
40320
>>> 
