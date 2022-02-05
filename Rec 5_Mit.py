### Creating a person
###
def make_person(name, age, height, weight):
    person = {}
    person['name']= name
    person['age']= age
    person['height']= height
    person['weight']= weight
    return person
def get_name(person):
    return person['name']
def set_name(person, name):
    person['name']= name
def get_age(person):
    return person['age']
def set_age(person, age):
    person['age']= age
def get_height(person):
    return person['height']
def set_height(person, height):
    person['height']= height
def get_weight(person):
    return person['weight']
def set_height(person, height):
    person['weight']= weight
def print_person(person):
    print ('Name:', get_name(person), ', Age:', get_age(person),  ', Height:', get_height(person),  ', Weight:', get_weight(person))

mitch = make_person('Mitch', 32, 70, 200)

##sarina = make_person('Sarina', 25, 65, 130)
##print_person(mitch)
##print(mitch)
##set_age(mitch, 25)
##print_person(mitch)
##print(type(mitch))
#### what about equality?
##def people_equal(person1, person2):
##    return get_name(person1) == get_name(person2)
##print (people_equal(sarina, mitch))
##
##class Person(object):
##    def _init_(self, name, age, height, weight):
##        self.name = name
##        self.age = age
##        self.height = height
##        self.weight = weight
### This type of method is called an accessor (or getter)
##    def get_name(self):
##    return self.name
### This type of method is called a mutator (or setter)
##    def set_name(self, name):
##    self.name = name

        
