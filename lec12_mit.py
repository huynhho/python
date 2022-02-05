import random
class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY): # if you give me a change in x and a change in y ,I'll give you back the new location,
        #which is to go from my x and y by some amount
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY) # It returns a new instance of a Location.
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distFrom(self, other):  # remember, self will point to my instance 
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    def __str__(self):
        return '<' + str(self.x) +',' + str(self.y) +'>'
##hoan = Location(3,4)
##print(hoan)
# a field is just going to be a collection of drunks, keeping track of where they are.
class Field(object): # a field is basically going to be something that maps drunks to location
    def __init__(self): # sets up a variable inside of that instance, just called drunks and we're going to use a dictionary
        self.drunks = {}
    def addDrunk(self, drunk, loc):                                   # I can add a drunk to the field.
        if drunk in self.drunks:                                      # It chesks to make sure that I don't already have this person in my collection.   
            raise ValueError('Duplicate drunk')                       # if this particular drunk is already in my dictionary, I complain.
        else:
            self.drunks[drunk] = loc                                  # a dictionary of drunks and  where they are.
    def moveDrunk (self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()                               # that's going to give me back a change in x and a change in y.
        self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)#therighthandsidesays,iget the dictionaryofdrunks,igoinandindex into it to get out the actual drunk.
                            # that's this first part right here. That gives me back what?. It gives me an instance
                            # so the dot says, for that particular drunk, get its move method, which was that call, and have it move by that amount.
                            # and that returns for me then a location which i can store back into the list
    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

# there's the definition of the drunk 

class Drunk(object):
    def __init__(self, name):
        self.name = name
    def takeStep(self):
        stepChoices = [(0,1), (0,-1),(1,0), (-1,0)]
        return random.choice(stepChoices)
    def __str__(self):
        return 'This drunk is named '+ self.name
def walk(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(start.distFrom(f.getLoc(d)))
           
def simWalks(numSteps, numTrials):
    homer = Drunk('Homer')
    origin = Location(0,0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numTrials))
    return distances
           
def drunkTest(numTrials):
    for numSteps in [10, 100, 1000, 10000, 100000]:
        distances = simWalks(numSteps, numTrials)
        print('Random walk of' + str(numSteps) + 'steps')
        print(' Mean =', sum(distances)/ len(distances))
        print(' Max =', max(distances), 'Min =', min(distances))
           
