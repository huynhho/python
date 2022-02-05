
def F(C):
	return (9/5)*C + 32
a = 10
F1 = F(a)
temp = F(15.5)
#print(F(a+1))
sum_temp = F(10)+ F(20)
#print(sum_temp)
#print(F1)
#print(F(a))

def F2(C):
	F_value = (9/5)*C + 32
	return '%.1f degrees Celsius corresponds to %.1f degrees Fahrenheit' % (C, F_value)
s1 = F2(21)
#print(s1)


def F3(C):
	F_value = (9/5)*C + 32
	return '{} degrees Celsius corresponds to {} degrees Fahrenheit'.format(C, F_value)
s1 = F3(21)
#print(s1)

def F3(C):
	F_value = (9/5)*C + 32
	print('Inside F3: C=%s F_value=%s r=%s' % (C, F_value, r))
	return '{} degrees Celsius corresponds to {} degrees Fahrenheit'.format(C, F_value)

C= 60
r = 21
s3 = F3(r)
print(s3)