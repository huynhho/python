Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def cube(x): return x*2

>>> cube(x)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    cube(x)
NameError: name 'x' is not defined
>>> cube(2)
4
>>> map(cube, range(10))
<map object at 0x02EECE30>
>>> def cube(x): return x*2

>>>  map(cube, range(10))
 
SyntaxError: unexpected indent
>>> def cube(x): return x*3

>>> map(cube, range(1,10))
<map object at 0x02A1C1D0>
>>> y=[1,2,3]
>>> map(cube,y)
<map object at 0x02EECDD0>
>>> map(cube(x),y)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    map(cube(x),y)
NameError: name 'x' is not defined
>>> x=[2,4,6]
>>> map(cube(x),y)
<map object at 0x02EECE90>
>>> a=range(1,10)
>>> a
range(1, 10)
>>> map(cube,a)
<map object at 0x02A1C1D0>
>>> def f(x): return x % 3 == 0 or x % 5 == 0

>>> f(x)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    f(x)
  File "<pyshell#20>", line 1, in f
    def f(x): return x % 3 == 0 or x % 5 == 0
TypeError: unsupported operand type(s) for %: 'list' and 'int'
>>> f(2)
False
>>> f(15)
True
>>> filter(f, range(2, 25))
<filter object at 0x02A1C1D0>
>>> matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
 ]
>>> matrix
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
>>> matrix2 = [
    [0, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
 ]
>>> matrix2
[[0, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
>>> matrix * matrix2
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    matrix * matrix2
TypeError: can't multiply sequence by non-int of type 'list'
>>> 2*matrix
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> basket
{'orange', 'banana', 'pear', 'apple'}
>>> ability = {'apple','concept'}
>>> basket and ability
{'concept', 'apple'}
>>> ability
{'concept', 'apple'}
>>> basket ^ ability
{'orange', 'concept', 'banana', 'pear'}
>>> basket & ability
{'apple'}
>>> basket - ability
{'orange', 'pear', 'banana'}
>>> basket | ability
{'orange', 'apple', 'concept', 'banana', 'pear'}
>>> set('abracadabra')
{'d', 'c', 'b', 'a', 'r'}
>>> set('hoan')
{'h', 'o', 'n', 'a'}
>>> set(hoan)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    set(hoan)
NameError: name 'hoan' is not defined
>>> set(122)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    set(122)
TypeError: 'int' object is not iterable
>>> set('12233)
    
SyntaxError: EOL while scanning string literal
>>> set('122')
{'1', '2'}
>>> compound nouns = {'active role','extended family','family gathering','immediate family','maternal instinct'}
SyntaxError: invalid syntax
>>> compound_nouns = {'active role','extended family','family gathering','immediate family','maternal instinct'}
>>> compound_nouns
{'maternal instinct', 'active role', 'immediate family', 'family gathering', 'extended family'}
>>> compound_nouns2={'sibling rivalry','stable upbringing', 'striking resemblance'}
>>> compound_nouns2
{'sibling rivalry', 'stable upbringing', 'striking resemblance'}
>>> compound_nouns | compound_nouns2
{'family gathering', 'striking resemblance', 'stable upbringing', 'active role', 'immediate family', 'extended family', 'sibling rivalry', 'maternal instinct'}
>>> True | False
True
>>> set(range(22))
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}
>>> compound_nouns & set(range(22))
set()
>>> squares = [x**2 for x in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> a = {x for x in 'abracadabra'}
>>> a
{'d', 'c', 'b', 'a', 'r'}
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'d', 'r'}
>>> hoan
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    hoan
NameError: name 'hoan' is not defined
>>> # hoan
>>> type(squares)
<class 'list'>
>>> type(a)
<class 'set'>
>>> type(compound_nouns)
<class 'set'>
>>> type(matrix)
<class 'list'>
>>> 
