# each employee is  going to have a name, email address, a pay, and also actions that they can perform
class Employee:
    pass # skip that for now
# now we have a simple employee class with no attributes or methods
# our class is basically ... for creating instances and
# each unique employee that we create using our employee class will be an instance of that class
emp_1 = Employee()
emp_2 = Employee()
print(emp_1)
print(emp_2)


# each of these are going to be their own unique instances of the employee class
# print both of these out and copy
# you can see that both of these are employee objects and they're both unique,
# they both have different locations here in memory
# this is an important distinction because you'll hear me talk a lot about instance variables and class variables
# and it's important to know the difference between those and I'll go more in depth into class variables in the next video

# INSTANCE VARIABLES: contain DATA that is unique to each instance.
# we could manually create instance variables for each employee by doing something like this
# let's say we wanted employee_1 to have a first name and a last name
emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000
# let's give employee_2 some of these same attributes
emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60000
# each of these instances have attributes that are unique to them
print(emp_1.email)
print(emp_2.email)
##class Employee:
##    def __init__(self): # think of this method as initialized  (constructor)
        # when we create methods within a class, they received the instance  as the first argument automatically





