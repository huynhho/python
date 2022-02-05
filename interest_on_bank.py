# A0 is the initial amount of money,
# A is the present amount after n days with p percent annual interest rate.
from math import log as ln

def present_amount(A0, p, n):
    return A0*(1+ p/(360*100))**n
def initial_amount(A, p, n):
    return A*(1 + p/(360*100))**(-n)
def days(A0, A, p):
    return ln(A/A0)/ln(1+p/(360*100))
