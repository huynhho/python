##def outer_function():
##    message = 'Hi'
##
##    def inner_function():
##        print(message)
##    return inner_function()
##
##my_func = outer_function()
##my_func()
##my_func()
##my_func()


# Decorators

##def decorator_function(original_function):
##    def wrapper_function():
##        print('wrapper executed this before:{} '.format(original_function.__name__)
##        return original_function()
##    return wrapper_function
##
##
##@decorator_function
##def display():
##    print('display function ran')
##import turtle
##
##def draw_square():
##    window = turtle.Screen()
##    window.bgcolor('red')
##
##    brad = turtle.Turtle()
##    brad.shape('turtle')
##    brad.color('yellow')
##    brad.speed(2)
##
##    brad.forward(100)
##    brad.right(90)
##    brad.forward(100)
##    brad.right(90)
##    brad.forward(100)
##    brad.right(90)
##    brad.forward(100)
##    brad.right(90)
##
##    window.exitonclick()
##
##draw_square()

nums = [1,2,3,4,5,6,7,8,9,10]
# I want 'n' for each 'n' in nums
##my_list = []
##for n in nums:
##    my_list.append(n)
##    print(n)
##    print(my_list)
##print(my_list)
my_list = [n for n in nums]
print(my_list)


    
