# If statements allow you to specify code that only executes if a specific conditon is true

##answer = input("Would you like express shipping?")
##if answer == "yes" or 'YES' or 'Yes':
##    print("That will be an extra $10")
##print("Have a nice day")
    
# I'm storing the value they gave me intto the variable answer.
# we use the equal sign to mean take this value, put it in here.
# so we say take the result of our input command, our input fuction.
# put it into the variable answer.

##bestTeam = 'senators'
##favouriteTeam = input('What is your favourite hockey team? ')
##if favouriteTeam.upper() == bestTeam.upper():# that generally is the best way to approach this
##    print("Yeah Go Sens Go")
##print("It's okay if you prefer football/soccer")
### What if we try an if statement with numbers instead of strings
##
##deposit = 150
##if deposit > 100:
##    print('You get a free toaster!')
##print('Have a nice day')



### We have to convert the string value returned by the input function to a number
##deposit = input('how much would you like to deposit?')
##if float(deposit) > 100:
##    print('you get a free toaster!')
##print('Have a nice day')
##
### Here is another way to do the same thing
##deposit = float(input('how much do you want to deposit '))
##if deposit >100:
##    print('enjoy your toaster')
##print('have a nice day')
### What if you get a free toaster for over $100 and a free mug for under $100

##deposit = input('How much would you like to deposit? ')
##if float(deposit) > 100:
##    print("you get a free toaster!")
##else:
##    print("Enjoy your mug!")
##print("Have a nice day")

# you can use boolean variables to remember if a condition is true or false
# It's always a good idea to initialize your variables!
# Initialize the variable to fix the error
freeToaster = False
deposit = input('how much would you like to deposit? ')
if float(deposit) > 100:
    # set the boolean variable freeToaster to True
    freeToaster = True

#if the variable freeToaster is True
#the print statement will execute
if freeToaster:
    print('enjoy your toaster')
print('Have a nice day!')
# Aren't you just making the code more complicated by using the Boolean variable?
# That depends
# What if you are writing a program, and there is more than one place you
# have to check that condition? You could check the condition once and
# remember the result in the Boolean variable
