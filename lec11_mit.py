class intSet(object):
    #An intSet is a set of integers
    def __init__(self):
        """Create an empty set of integers"""
        self.numBuckets = 47
        self.vals = []
        for i in range(self.numBuckets):
            self.vals.append([])
s = intSet()
print(s.numBuckets)
            
print(s.vals)

def test():
    s = intset()
    for i in range(40):
        s.insert(i)
    print(s.member(14))
    print(s.member(41))
    print (s)
    print (s.vals)
