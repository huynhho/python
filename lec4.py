
######print (withinEpsilon(2,3,1))
######val = withinEpsilon(2,3,0.5)
######print (val)
####def f(x):
####    x = x + 1
####    print ('x =',x)
####    return x
####x = 3
####z = f(x)
####print ('z=',z)
##def f1(x):
##    def g():
##        x = 'abc'
##    x = x +1
##    print ('x=', x)
##    g()
##    assert False
##    return x
##x = 3
##z = f1(x)
##print (z)
def withinEpsilon(x, y, epsilon):
    """x,y, epsilon ints or floats. epsilon > 0.0
       returns true if x is within epsilon of y"""
    return abs(x-y) <= epsilon

def isEven(i):
    """ assumes i a positive int
        returns True if i is even, otherwise False"""
    return i%2 == 0

def findRoot (pwr, val, epsilon):
    """ assumes pwr an it; val, epsilon floats
        pwr and epsilon > 0
        if it exists,
        returns a value within epsilon of val**pwr
        otherwise returns None"""
    assert type(pwr) == int and type(val) == float and type(epsilon) == float
    assert pwr > 0 and epsilon >0
    if isEven(pwr) and val <0:
        return 'Hoan is handsome'
    low = -abs(val)
    high = max(abs(val), 1.0)
    ans = (high + low)/ 2.0
    print(withinEpsilon(ans**pwr, val, epsilon))
    while not withinEpsilon(ans**pwr, val, epsilon):
        print ('ans =', ans, 'low =', low, 'high =', high)
        if ans**pwr < val:
            low = ans
        else:
            high = ans
        ans =(high + low)/2.0
    return ans
print(findRoot(pwr = 3,val = -2.5,epsilon = 0.5))
def testFindRoot():
    """ x float, epsilon float, pwr positive int """
    for x in (-1.0, 1.0, 3456.0):
        for pwr in (1, 2, 3):
            ans = findRoot(pwr, x, 0.001)
            if ans == None:
                print('The answer is imaginary')
            else: print (ans, 'to the power', pwr, 'is close to x',x)
