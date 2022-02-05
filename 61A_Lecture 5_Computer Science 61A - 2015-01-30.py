##def f(x,y):
##    return g(x)
##
##def g(a):
##    return a + y
##f(1, 2)



def square(x):
    return x * x
    
def triple(x):
    return 3 * x
    
def compose(f, g):
    def h(x):
        return f(g(x))
    return h
print(square(4))
print(triple(5))
cute = compose(triple, square)
result = cute(5)
print(result)
