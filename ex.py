"""Generalization."""
##from math import pi, sqrt
##
##def area(r, shape_constant):
##    assert r > 0, 'A length must be positive'
##    return r*r*shape_constant
##def area_square(r):
##    return area(r, 1)
##
##def area_circle(r):
##    return area(r, pi)
##
##def area_hexagon(r):
##    
##    return area(r, 3*sqrt(3)/2)



def identity(k):
    return k
def cube(k):
    return pow(k, 3)
def summation(n, term):
    total, k = 0,1
    while k<=n:
        total, k = total + term(k), k+1
    return total

def sum_naturals(n):
    return summation(n, identity)
def sum_cubes(n):
    return summation(n, cube)
##
##def sum_naturals(n):
##    """Sum the first N natural numbers.
##     >>> sum_naturals(5)
##     15
##    """
##    total, k = 0, 1
##    while k<=n:
##        total, k = total + k, k+1
##    return total
##
##def sum_cubes(n):
##    total, k= 0, 1
##    while k<=n:
##        total, k = total + pow(k,3), k+1
##    return total
