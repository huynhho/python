def split(n):
    """Split positive n into all but its last digit and its last digit."""
    return n // 10, n % 10

def sum_digits(n):
    """Return the sum of the digits of positive integer n."""
    if n < 10:
        print(n)
        return n
    else:
        all_but_last, last = split(n)
        print('sum_digits(all_but_last): ',sum_digits(all_but_last))
        print('last: ', last)
        return sum_digits(all_but_last) + last
##print(sum_digits(146))
print(sum_digits(15555))


##def fact(n):
##    if n == 0:
##        return 1
##    else:
##        print('n: ',n)
##        return n * fact(n-1)
##fact(3)    
