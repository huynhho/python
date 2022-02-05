### Global scope
##X = 99  # X and func assigned in module: global
##
##def func(Y):  # Y and Z assigned in function: locals
##    # Local scope
##    Z = X + Y # X is a global
##    return Z
##print(func(1)) # func in module: result = 100
##import builtins
##dir(builtins)
def increment(n):
    return n+1
def square(n):
    return n**2
##def findSequence(initial, goal):
##    # construct list of "candidates" of form ('1 increment increment', 3)
##    candidates = [(str(initial), initial)] # ['1',1]
####    print (candidates)
##    # loop over sequences of length "i" = 1, 2, 3,...
##    for i in range(1, goal-initial+1):     # range(1,10)
##        newCandidates = []
##        # construct each new candidate by adding one operation to prev candidate
##        for (action, result) in candidates:
##            #print(action, result)
##            for (a,r) in [(' increment',increment), (' square',square)]:
####                 print(a,r)
##                 newCandidates.append((action+a, r(result)))
####                 print(r(result))
####                 print(newCandidates)
####                 print(i, ':',newCandidates[-1])
##                 if newCandidates[-1][1] == goal:
##                     return newCandidates[-1]
##                
##                
##        candidates = newCandidates

##answer = findSequence(1,5)
##print ('answer =', answer)
##def apply(opList, arg):
##    if len(opList) ==0:
##        return arg
##    else:
##        return apply(opList[1:],opList[0](arg))
##    print(opList[1:])
##    print(opList[0](arg))
####print(apply([],7))
##print(apply([increment],7))
##print(apply([increment, square],7))
##print([increment, square][1:])
##print(apply([square],8))
##
class Node:
    def __init__(self, parent, action, answer):
        self. parent = parent
        self.action = action
        self.answer = answer
    def path(self):
        if self.parent == None:
            return [(self.action, self.answer)]
        else:
            return self.parent.path() + [(self.action, self.answer)]
    def findSequence(initial, goal):
        q = [(None,None,1)]
        while q:
            parent = q.pop(0)
            for (a,r) in [('increment', increment),('square', square)]:
                newNode = (parent,a,r(parent.answer))
                if newNode.answer == goal:
                    return newNode.path()
                else:
                    q.append(newNode)
        return None
    answer = findSequence(1, 100)
    print('answer=', answer)
 

                
                

        
