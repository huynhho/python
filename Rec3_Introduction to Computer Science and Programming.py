## dictionaries
# EXAMPLE 7: Recursion
# How might we make a factorial function?
def factorial(n):
    # if [base case is true] -> what ir the base case?
    if n == 0:
        # 0! is 1
        return 1
    else:
        return n* factorial(n-1)
#Test!
print (factorial(0))
print (factorial(4))
print (factorial(3))
