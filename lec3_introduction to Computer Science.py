###Find the cube root of a perfect cube
##x = int(input('Enter an integer:'))
##for ans in range(0, abs(x)+1):
##    if ans**3 == abs(x):
##        break
##print('ans:', ans)
##if ans**3 != abs(x):
##    print (x, 'is not a perfect cube')
##else:
##    if x < 0:
##        ans = -ans
##    print ('Cube root of ' +str(x) + ' is ', str(ans))
##x = 12345
##epsilon = 0.01
##numGuesses = 0
##ans = 0.0
##while abs(ans**2 - x) >= epsilon and ans <=x:
##    #print('ans =', ans)
##    ans +=1
##    #ans += 0.00001
##    numGuesses +=1
##print ('numGuesses =', numGuesses)
##if abs(ans**2 - x) >= epsilon:
##    print ('Failed on square root of', x)
##else:
##    print (ans, 'is close to square root of', x)
##x=0.5
##epsilon = 0.01
##numGuesses = 0
##low = 0.0
##high = max(x,1)
##ans = (high + low)/2.0
##while abs(ans**2 - x) >= epsilon:
##    numGuesses +=1
##    print('ans  =', ans, 'low =', low, 'high = ',high)
##    if ans**2 < x:
##        low = ans
##    else:
##        high = ans
##    ans =(high + low)/ 2.0
##print (ans, 'is close to square root of',x)
##print('numGuesses =', numGuesses)
####x=155
##epsilon = 0.01
##low = 0.0
##high = x
##ans = (high + low)/2.0
##while abs(ans**3 - x) >= epsilon:
##    print('ans  =', ans, 'low =', low, 'high = ',high)
##    if ans**3 < x:
##        low = ans
##    else:
##        high = ans
##    ans =(high + low)/ 2.0
##print (ans, 'is close to cube root of',x)
##
##def withinEpsilon (x,y,epsilon):
##    """x, y, epsilon ints or floats. epsilon >0.0
##     return true if x is within epsilon of y"""
##    return abs(x-y) <= epsilon
##def f(x):
##    x = x+1
##    print ('x=',x)
##    return x
##x = 3
##z = f(x)
##print ('z=', z)
##print ('x=',x)
##def f1(x):
##    def g(x):
##        x = 'abc'
##        
##    x = x+1
##    print ('x=',x)
##    g(x)
##    assert False
##
##    return x
##x = 3
##z =f1(x)
##print(g(x))
##def isEven(i):
##    """assumes i a positive int
##       returns True if i is even, otherwise False"""
##    return i%2 == 0
##def findRoot(pwr, val, epsilon):
##    """assumes pwr an int; val, epsilon floats
##       pwr and epsilon >0
##       if it exists,
##       returns a value within epsilon of val**pwr
##       otherwise returns None"""
##    assert type(pwr) == int and type(val) == float\
##           and type(epsilon) == float
##    assert pwr > 0 and epsilon > 0
##    if isEven(pwr) and val < 0:
##        return None
##    low = -abs(val)
##    high = max(abs(val), 1.0)
##    ans = (high + low)/2.0
##    while not withinEpsilon(ans**pwr, val, epsilon):
##        #print ('ans =', ans, 'low =', low, 'high =', high)
##        if ans**pwr < val:
##            low = ans
##        else:
##            high = ans
##        ans = (high + low) /2.0
##    return ans
##sumDigits = 0
##for c in str(1952):
##    sumDigits += int(c)
##print (sumDigits)
x = 100
divisors = ()
for i in range(1,x):
##    print(i)
    if x % i == 0:
        divisors = divisors + (i,)
        print(divisors)
print (divisors[0] + divisors[1])
print (divisors[2:4])


    
