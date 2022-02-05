######while True:
######    try:
######        a = int(input('ntor: '))
######        b = int(input('dtor: '))
######        print('result: ', a/b)
######    except:
######        print('oops: try again: ')
######    else:
######        break
####from operator import add, sub
####
####def a_plus_abs_b(a, b):
####    """Return a+abs(b), but without calling abs.
####
####    >>> a_plus_abs_b(2, 3)
####    5
####    >>> a_plus_abs_b(2, -3)
####    5
####    """
####    if b < 0:
####        f = sub
####    else:
####        f = add
####    return f(a, b)
####print(a_plus_abs_b(3,4))
##
##def if_function(condition, true_result, false_result):
##    if condition:
##        return true_result
##    else:
##        return false_result
###print(if_function(3 == 100, 100-10, ' If you order before 12.00, the goods will arrive the next day'))
##def with_if_statement():
##    """
##    >>> with_if_statement()
##    1
##    """
##    if c():
##        return t()
##    else:
##        return f()
##
##def with_if_function():
##    return if_function(c(), t(), f())
##
##def c():
##    return False
##
##def t():
##    1/0
##
##def f():
##    return 1
##def largest_factor(n):
##    
##    factor = n - 1
##    while factor > 0:
##        if n % factor == 0:
##            return factor
##        factor -= 1
##def multiple(a, b):
##    """Return the smallest number n that is a multiple of both a and b.
##
##    >>> multiple(3, 4)
##    12
##    >>> multiple(14, 21)
##    42
##    """
##    "*** YOUR CODE HERE ***"
##   
##    return largest_factor(a) * largest_factor(b)
def fib(n):
    pred, curr = 0, 1
    k = 1
    while k<n:
        pred, curr = curr, pred + curr
        print( pred, curr)
        k = k + 1
    return curr
fib(11)

    
