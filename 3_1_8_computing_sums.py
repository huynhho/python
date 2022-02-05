##s=0
##for i in range(1,6):
##    s += i**2
##    print(s)
##    
##print(s)
##
##c =[]
##c_value = -50
##c_max = 200
##
##while c_value <= c_max:
##    c.append(c_value)
##    print(c)
##    c_value += 50
##    print(c_value)
##v0 = 5
##g = 9.81
##t = 0.6
##y = v0 * t - 0.5*g*t**2
###print("At t=%f s, a ball with initial velocity v0=%.3E m/s is located at the height %.2f m." %(t, v0, y))
##print('At t={t:g} s, the height of the ball is {y:.2f} m.'.format(t=t,y=y))
##print('y(t) is the position of our ball.')
##print('y(t) is\nthe position of\nour ball')
##
##import math
##print(math.sqrt(2))
##from math import log10 as Hoaniscute
###print(sqrt(16))
##print(Hoaniscute(100))
##def outer_function(msg):
##    message = msg
##
##    def inner_function():
##        print(message )
##    return inner_function
###outer_function()
##hoan1 = outer_function('Hi Hoan')
##hoan2 = outer_function('Bye Hoan')
##
##hoan1()
##hoan2()
x = 1.2 # assign some value
N = 25  # maxium power in sum
k =1
s = x
sign = 1.0
import math

while k<N:
    sign = -sign
    k = k+2
    print(sign)
    print(k)
    term = sign*x**k/math.factorial(k)
    print(term)
    s = s + term
    print(s )

print('sin(%g) = %g (approximation with %d terms)' %(x,s,N))
