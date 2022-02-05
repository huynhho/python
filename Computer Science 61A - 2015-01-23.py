##f = min
##f = max
##g, h = min, max
##max = g
##print(max(f(2, g(h(1, 5), 3)), 4))
##


from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)
#print(a_plus_abs_b(2,3))
def two_of_three(a, b, c):
    return max(a, b, c)* max(a, b, c) 

#print(two_of_three(2,3,4))
#print(two_of_three(-3,0,-5))

class Link:
    """A linked list with a first element and the rest."""
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]
    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0},{1})'.format(self.first, rest_str)

    def second(self):
        return self.rest.first
s = Link(3, Link(4, Link(5)))



square = lambda x: x * x
odd = lambda x: x % 2 == 1



s = Link(6, Link(7, Link(8)))
step = Link(44, Link(45, Link(46, Link(47))))
combine_Links = Link(s, step)
combine = Link(s, Link(1000))
#print(combine_Links)
#print(s)
#print(s[1])
#print('s[1]:', s[1])
#print('step[1]:', step[1])
#print('step[2]:', step[2])



def link_expression(s):
    """Return a string that would evaluate to s."""
    if s.rest is Link.empty:
        rest = ''
    else:
        rest = ', ' + link_expression(s.rest)
    return 'Link({}{})'.format(s.first, rest)

def extend_link(s,t):
    if s is Link.empty:
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))
#print(extend_link(s,s))  


#print(link_expression(s))
#print(link_expression(step))
#print(link_expression(combine_Links))
#print(link_expression(combine))
#Link.__repr__ = link_expression
#print(s)
#s_first = Link(s, Link(3333))
#print(s_first)
#print(extend_link(s,s))  
def square(x):
    return x*x
def map_link(f, s):
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))
#print(map_link(square, s))


def sum_digits(n):
    """Return the sum of the digits of positive integer n."""
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last

class Tree:
    """A tree is a label and a list of branches"""
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches) 

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self, k=0):
        indented = []
        for b in self.branches:
            for line in b.indented(k+1):
                indented.append('' + line)
        return [str(self.label)] + indented

    def is_leaf(self):
        return not self.branches


#print(Tree(20))
#print(Tree(22, [Tree(33)]))
#print(Tree(22, [Tree(33), Tree(333335)]))



def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])
# Linked lists have recursive structure: the rest of a linked list is a linked list or 'empty'.
empty = 'empty'
def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))



def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element."
    return s[0]
def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), "rest only applies to linked lists."
    assert s != empty, "empty linked list has no rest."
    return s[1]

def len_link(s):
    """Return the length of linked list s."""
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length

def getitem_link(s, i):
    """Return the element at index i of linked list s."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)

def len_link_recursive(s):
    """Return the length of a linked list s."""
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))
def getitem_link_recursive(s, i):
    """Return the element at index i of linked list s."""
    if i == 0:
        return first(s)
    return getitem_link_recursive(rest(s), i - 1)

def extend_link(s, t):
    """Return a list with the elements of s followed by those of t."""
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))

def keep_if_link(f, s):
    """Return a list with elements of s for which f(e) is true."""
    assert is_link(s)
    if s == empty:
        return s
    else:
        kept = keep_if_link(f, rest(s))
        if f(first(s)):
            return link(first(s), kept)
        else:
            return kept
def join_link(s, separator):
    """Return a string of all elements in s separated by separator."""
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)

four = link(1, link(2, link(3, link(4, empty))))
#print(first(four))
#print(rest(four))
      
#print(join_link(four, ","))            




def count(s, value):
    """Count the number of occurrences of value in sequence s."""
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total = total + 1
        index = index + 1
    return total




def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n) 
    counted.call_count = 0
    return counted
fib = count(fib)
#print(fib(5))           
#print(fib.call_count)

list = [23,444,5555, 333566677777]
#print(list[:2]) # [5555,  333566677777] wrong
#print(list[1:]) # [23,444]

# Θ(log n) : Logarithmic growth 

def search(lst, value):
    if len(lst) == 1:
        return lst[0] == value
    mid = lst[len(lst) // 2]
    if value < mid:
        return search(lst[:mid], value)
    else:
        return search(lst[mid:], value)

#print(search(List, 4))

def sum_lst(lst):
    if lst == []:
        return 0
    else:
        return lst.pop() + sum_lst(lst)
List = [2,33333, 4]        

sequoia = 99 + 1
redwood = 50.
sequoia * redwood
stick = int(sequoia // redwood)
stick *= "Tree "
x = 5
def increment():
    y = x + 1


#print(hoan)
#print(increment())

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        #self.email = first + '.' + last + '@email.com'
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amt)

    def __repr__(self):
        return "Employee('{}','{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} = {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())



emp_1 = Employee('hoan', 'huynh', 50000)
emp_2 = Employee('han', 'huynh', 60000)
#print(repr(emp_1))
#print(str(emp_1))
#print(emp_1.__repr__())
#print(emp_1.__str__())
#print(int.__add__(4,55))
#print(str.__add__('tutorial' , 'special'))
#print('special'.__len__())
# print(emp_1 + emp_2)

# print(repr(emp_2))
# print(len(emp_2))
# print("First Module's Name: {}".format(__name__))
# print(__name__)

# import unittest
# import sys
# print(sys.executable)

emp_1.fullname = 'Corey Schafer'
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname






import time as _time 
import math as _math 
def _cmp(x,y):
    return 0 if x ==y else 1 if x>y else -1
MINYEAR = 1
MAXYEAR = 9999
_MAXORGIANL = 3652059

def square(x):
    return x*x
def sum_square_up_to(n):
    k = 1
    total = 0
    while k <= n:
        total, k = total + square(k), k + 1
    return total
# print(sum_square_up_to(5))

# print(1**2 + 2**2 + 3**2 + 4**2 + 5**2)

def fib(num):
    a, b = 0, 1
    for i in xrange(o, num):
        yield '{}: {}'.format(i+1, a)
        a, b = b, a + b

from math import sin, sqrt, pi, exp
result = [sin(i) for i in [1,2,3]]
#print(result)


def normal_distribution(x, u=0, o=1):
    z = (-(x-u)**2)/(2*o**2)
    result = (1/sqrt(2*pi*o**2))* exp(z)
    return result
# print(normal_distribution(0,5,10)) 
# print(normal_distribution(-0.01114576,0,1))   
# print(normal_distribution(0.37901987))

def bubble_sort(L):
    swap = False
    while not swap:
        print('buble sort:' + str(L))
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
 


lst = [2,3,6,1,10,9]
#bubble_sort(lst)

def selection_sort(L):
    s = 0
    while s != len(L): 
        print('selection sort: ' + str(L))
        for i in range(s, len(L)):
            if L[i] < L[s]:
                L[s], L[i] = L[i], L[s]
        s += 1
selection_sort(lst)