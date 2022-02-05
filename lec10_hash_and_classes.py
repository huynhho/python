numBuckets = 47 # this is ugly. We will see a better way soon
def create():
    global numBuckets
    hSet = []
    for i in range(numBuckets):
        hSet.append([])
    return hSet
def hashElem(e):
    global numBuckets
    return e % numBuckets
def insert(hSet, i):
    hSet[hashElem(i)].append(i)
##    print (hSet)
def remove(hSet, i):
    newBucket =[]
    for j in hSet[hashElem(i)]:
        if j != i :
            newBucket.append(j)
    hSet[hashElem(i)] = newBucket
##    print(hSet)
def member(hSet, i):
    return i in hSet[hashElem(i)]

numBuckets = 47
def test1():
    s = create()
    for i in range(40):
        insert(s, i)
    insert(s, 325)
    insert(s, 325)
    insert(s, 987654321)
    print (s)
    #assert False
    print (member(s, 325))
    remove(s, 325)
    print(member(s, 325))
    print(member(s, 987654321))
print(test1())



##class intSet(object): # define a new abstract type called intSet
##    # An intSet is a set of integers
##    def __init__(self): # I've got this funny method called underbar underbar init.
##        #Whenever you see something with an underbar underbar in its name, it has a special status in Python that lets us do elegant things with the syntax.
##        #What will happen every time I create a new object of type intSet, __init__ method, or function, of the class will be executed on that object.
##        # What it will do, in this case, is troduce two attributes of the object.
##        # The attributes are numBuckets which is now replacing the global variable we looked at last time.
##        # and vals-this will be the hash table itself containing the values.
##        """Create an empty set of integers"""
##        self.numBuckets = 47
##        self.vals = []
##        for i in range(self.numBuckets):
##            self.vals.append([])
##
##    def hashE(self, e):
##        #Private function, should not be used out side of class
##        return abs(e) % len(self.vals)
##    def insert(self, e):
##        """Assumes e is an integer and inserts e into self"""
##        for i in self.vals[self.hashE(e)]:
##            if i == e: return 
##        self.vals[self.hashE(e)].append(e)
##    def member(self, e):
##        """Assumes e is an integer
##           Returns True if e is in self, and False otherwise"""
##        return e in self.vals[self.hashE(e)]
##    def __str__(self):
##        """Returns a string representation of self"""
##        elems = []
##        for bucket in self.vals:
##            for e in bucket: elems.append(e)
##        elems.sort()
##        result = ''
##        for e in elems: result = result + str(e) + ','
##        return '{' + result[:-1] + '}'
##def test():
##    s = intSet()
##    for i in range(40):
##        s.insert(i)   # This s before the dot is actually the first argument to the method insert.
##    print(s.member(14))
##    print (s.member(41))
##    print(s)
##    print(s.vals) # Evil

##def readVal(valType, requestMsg, errorMsg):
##    numTries = 0
##    while numTries < 4:
##        val = input(requestMsg)
##        try:
##            val = valType(val)
##            return val
##        except ValueError:
##            print(errorMsg)
##            numTries +=1
##    raise TypeError('Num tries exceeded -Hoan is so handsome')
##
##
####print(readVal(int, 'Enter int:', 'Not an int.'))
##try:
##    readVal(int, 'Enter int:', 'Not an int.')
##except TypeError , s:
##    print(s)

# The idea I want to convey here is how we use classes and abstract date types to design programs.
##import datetime
# Person was a subclass of object
##class Person(object):
##    def __init__(self, name):
##        # create a person with name name
##        self.name = name
##        try:
##            firstBlank = name.rindex(' ')
##            self.lastName = name[firstBlank + 1:] # hard 
##        except:
##            self.lastName = name
##        self.birthday = None
##    def getLastName(self):
##        # return self's last name
##        return self.lastName
##    def setBirthday(self, birthDate):
##        # assumes birthDate is of type datetime.date
##        # sets self's birthday to birthDate
##        assert type(birthDate) == datetime.date
##        self.birthday = birthDate
##    def getAge(self):
##        # assumes that self's birthday  has been set
##        # returns self's current age in days
##        assert self.birthday != None
##        return (datetime.date.today() - self.birthday).days
####    def __lt__(self, other):
####        # return True if self's name is lexicographically greateer
####        # than other's name, and False otherwise
####        if self.lastName == other.lastName:
####            return self.name < other.name
####        return self.lastName < other.lastName
##    def __str__(self):
##        #return self's name
##        return self.name
##me = Person('John Guttag')
##him = Person('Barack Hussein Obama')
##her = Person('Madonna')
##hoan = Person('Hoan Van Huynh')
##han = Person ('Han Van Huynh')
##print(him)
##print(him.getLastName())
##print(her.getLastName())
##print(me.getLastName())
##print(hoan.getLastName())
##print(han.getLastName())
##him.setBirthday(datetime.date(1961, 8, 4))
##her.setBirthday(datetime.date(1958, 8, 16))
##print(him.getAge())
##print(her.getAge())
##print( him < her)
##print( me < her)
##print(han < hoan)
##print(hoan < han)
##pList = [me, him, her]
##print('The people in plist are:')
##for p in pList:
##    print(p)
##pList.sort()
##print('The people in plist are:')
##for j in pList:
##    print(j)

 #I'm going to start using the hierarchy
 #MIT person is a special subclass of person.
 #So it has all of the properties of a person.
##class MITPerson(Person):
##    nextIdNum = 0 #is not associated with an instance of MIT person
##    #, but it's associated with the class itself.It's a class variable.
##    def __init__(self, name):
##        Person.__init__(self, name)
##        self.idNum = MITPerson.nextIdNum
##        MITPerson.nextIdNum += 1
##    def getIdNum(self):
##        return self.idNum
##    def __lt__(self, other):
##        return self.idNum < other.idNum
##    def isStudent(self):
##        return type(self) == UG or type(self) ==G
####p1 = MITPerson('Barbara Beaver')
##p2 = MITPerson('Sue Yuan')
##p3 = MITPerson('Sue Yuan')
##print('p1 =' ,p1, p1.getIdNum())
##print('p2 =' ,p2, p2.getIdNum())
##print('p3 =' ,p3, p3.getIdNum())
##p4 = Person('Sue yuan')
##print('p1 < p2 =', p1 < p2)
##print('p3 < p2 =', p3 < p2)
## what this says is don't use the less than of the subclass.
## Go up and use the super class one to do the comparison.
##print('__lt__(p1, p2) =', Person.__lt__(p1, p2))
##print(Person.__lt__(p1, p2))
##print('p1 == p4 =', p1 == p4)
##print('p4 < p3 =',  p4 < p3) #hard
##print('p3 < p4 =', p3 < p4)

    # a subclass of an MIT person, called an UG, short for undergraduate
##    
##class UG(MITPerson):
##    def __init__(self, name):
##        MITPerson.__init__(self, name)
##        self.year = None
##    def setYear(self, year):
##        if year > 5:
##            raise OverflowError('Too many')
##        self.year = year
##    def getYear(self):
##        return self.year()
##ug1 = UG('Jane Doe')
##ug2 = UG('Jane Doe')
##p3 = MITPerson('Sue Yuan')
####print('ug1 =' ,ug1, ug1.getIdNum())
####print('ug2 =' ,ug2, ug2.getIdNum())
####print('ug3 =' ,ug3, ug3.getIdNum())
####
####
####print('p3 =' ,p3, p3.getIdNum())
####
####print(ug1)
####print(ug1 < p3)
####print(ug2 < ug1)
####print(ug1 == ug2)
##class G(MITPerson):
##    pass
##g1 = G('Mitch Peabody')
##print(g1.isStudent())

# another class
    
##class CourseList(object):
##    def __init__(self, number): # create an instance of a course list
##        self.number = number
##        self.students = []
##    def addStudent(self, who):
##        if not who.isStudent():
##            raise TypeError('Not a student')
##        if who in self.students:
##            raise ValueError('Duplicate studen')
##        self.students.append(who)
##    def remStudent(self, who):
##        try:
##            self.students.remove(who)
##        except:
##            print(str(who) + ' not in ' + self. number)
##    def allStudents(self):
##        for s in self.students:
##            yield s
##    def ugs(self):
##        indx = 0
##        while indx < len(self.students):
##            if type(self.students[indx]) == UG:
##                yield self.students[indx]
##            indx +=1
##
####class G(MITPerson):
####    pass
##m1 = MITPerson('Barbara Beaver')
##ug1 = UG('Jane Doe')
##ug2 = UG('John Doe')
##g1 = G('Mitch Peabody')
##g2 = G('Ryan Jackson')
##g3 = G('Sarina Canelake')
##SixHundred = CourseList('6.00')
##SixHundred.addStudent(ug1)
##SixHundred.addStudent(g1)
##SixHundred.addStudent(ug2)



            
        
        

     
