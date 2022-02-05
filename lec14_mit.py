import random
def rollDie():
    return random.choice([1,2,3,4,5,6])
def checkPascal(numTrials = 100000):
    yes = 0.0
    for i in range(numTrials):
        for j in range(24):
            d1 = rollDie()
            d2 = rollDie()
            if d1 ==6 and d2 ==6:
                yes +=1
                break
    print('Probability of losing = ' + str(1.0 - yes/numTrials))
##checkPascal()
##print((35/36)**24)
##                
def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        if random.random()<0.5:
            heads +=1
    return heads/float(numFlips)
##print(flip(10))
##print(flip(1000000))



def flipPlot(minExp, maxExp):
    ratios = []
    diffs = []
    xAxis = []
    for exp in range(minExp, maxExp +1):
        xAxis.append(2**exp)
        print(xAxis)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.random()<0.5:
                numHeads +=1
        print(numHeads)
        numTails = numFlips-numHeads
        print(numTails)
        ratios.append(numHeads/float(numTails))
        print(ratios)
        
        diffs.append(abs(numHeads -  numTails))
        print(diffs)
flipPlot(4,20)
##
##def flipSim(numFlipsPerTrial, numTrials):
##    fracHeads = []
##    for i in range(numTrials):
##        fracHeads.append(flip(numFlipsPerTrial))
##    mean = sum(fracHeads)/float(len(fracHeads))
##    return (mean)
