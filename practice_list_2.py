
leisure_activities=('football','swimming','going to the gym')
def translateWord(football, leisure_activities):
    if football in leisure_activities:
        return leisure_acttivities[football]
    else:
        return football
for x in leisure_activities :
    print (x, 'is in leisure_activities')
Test = (1,2,3,4,5)
print(Test[0])
print (Test[1])

print(' you should study English every day')           
x=100
divisors = ()
for i in range(1,x):
    if x%i == 0:
        divisors = divisors + (i,)
        print (divisors)

print ('pay close attension')
x=100
divisors = ()
for i in range(1,x):
    if x%i == 0:
        divisors = divisors + (i,)
print (divisors)
Techs = ['MIT', 'Cal Tech']
Ivys = ['Harvard', 'Yale', 'Brown']
Univs =[]
Univs.append(Techs)
print ('Univs =', Univs)
Univs.append(Ivys)
print ('Univs = ', Univs)
for e in Univs:
    print('e = ',e)
flat = Techs + Ivys
print('flat =', flat)
artSchools = ['Hansome', 'Harvard']
for u2 in artSchools :
    if u2 in flat:
        flat.remove(u2)
print ('flat=',flat)
flat.sort()
print('flat=',flat)
flat[1]='handsome'
print('flat=',flat)

       
        
         
