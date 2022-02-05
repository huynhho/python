##x = 3 # Create variable x and assign value 3  to it
##x = x*x #Bind x to value 9
##print (x)
##y = int(input('enter a number: '))
##print (type(y))
##y = float(input('Enter a number:'))
##print (type(y))
##print (y*y)
####x = int(input('Enter an integer:'))
####if x%2 == 0:
####    print ('Even')
####else:
####    print ('Odd')
####    if x%3 !=0:
####        print ('And not divisible by 3')
##x = int(input('Enter x: '))
##y = int(input('Enter y: '))
##z = int(input('Enter z: '))
####if x < y:
####    if x < z:
####        print ('x is least')
####    else:
####        print ('z is least')
####else:
####    print ('y is least')
####if x < y:
####    if x <z:
####        print ('x is least')
####    else:
####        print ('z is least')
####elif y < z:
####    print ('y is least')
####else:
####    print ('z is least')
####
##if x < y and x <z:
##    print ('x is least')
##elif y < z:
##    print ('y is least')
##elif x == y and y ==z: # Hoan typed
##    print('x=y=z=',x)
##else:
##    print ('z is least')

# Find the cube root of a perfect cube
x = int(input('Enter an integer: '))
ans = 0
while ans*ans*ans < abs(x):
    ans = ans + 1
    print ('current guess = ', ans)
print('last guess = ',ans)
print('ans*ans*ans =', ans*ans*ans)
if ans*ans*ans != abs(x):
    print (x, 'is not a perfect cube')
    if x<0:
        print('You entered a negative number, pay attention!!')
    else:
        print(x, 'is a positive number')
else:
    if x < 0:
        ans = -ans
        print('You entered a negative number')
    print ('Cube root of ' + str(x) + ' is ' + str(ans))
    print('Congratulations on your nice job!')
## write a program that prints the numbers from 1 to 100. But for
# multiples of three print 'Fizz' instead of the number and for the
# multiples of five print 'Buzz'. For numbers which are multiples
# both three and five print 'FizzBuzz'.

##for i in range(1,100):
##    s = str(i)
####    if i%3 ==0 and/(or) i%5 ==0:
##        s = ''
##        if i%3 ==0:
##            s = s + 'Fizz'
##        if i%5 ==0:
##            s = s +'Buzz'
##    print (s)
##    
