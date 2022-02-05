Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=2
>>> b=3
>>> if (a > b):
   print "a is greater than b"
   print "blocks are defined by indentation"
elif (a < b):
   print "a is less than b"
else:
   print "a is equal to b"
   
SyntaxError: Missing parentheses in call to 'print'
>>> if (a > b):
   print ("a is greater than b")
   print ("blocks are defined by indentation")
elif (a < b):
   print ("a is less than b")
else:
   print ("a is equal to b")

   
a is less than b
>>> a=3
>>> b=2
>>> if (a > b):
   print ("a is greater than b")
   print ("blocks are defined by indentation")
elif (a < b):
   print ("a is less than b")
else:
   print ("a is equal to b")

a is greater than b
blocks are defined by indentation
>>> a=3
>>> b=3
>>> if (a > b):
   print ("a is greater than b")
   print ("blocks are defined by indentation")
elif (a < b):
   print ("a is less than b")
else:
   print ("a is equal to b")

a is equal to b
>>> a= 'popular'
>>> b='angry'
>>> len(a)
7
>>> len(b)
5
>>> if (len(a) > len(b)):
   print ("a is greater than b")
   print ("blocks are defined by indentation")
elif (len(a) < len(b)):
   print ("a is less than b")
else:
   print ("a is equal to b")

   
a is greater than b
blocks are defined by indentation
>>> group=['angry', 'nervous', 'worried']
>>> inagoodmood=[]
>>> inagoodmood.append(group)
>>> 
>>> inagoodmood
[['angry', 'nervous', 'worried']]
>>> len(group)
3
>>> len(inagoodmood)
1
>>> inagoodmood.append(inagoodmood)
>>> inagoodmood
[['angry', 'nervous', 'worried'], [...]]
>>> len(inagoodmood)
2
>>> excited=[]
>>> len(excited)
0
>>> for i in inagoodmood:
	print (i)

	
['angry', 'nervous', 'worried']
[['angry', 'nervous', 'worried'], [...]]
>>> Techs=['MIT', 'Cal Tech']
>>> Ivys=['Harvard','Yale','Brown']
>>> Univs=[]
>>> Univs.append(Techs)
>>> Univs
[['MIT', 'Cal Tech']]
>>> print('Univs',Univs)
Univs [['MIT', 'Cal Tech']]
>>> Univs.append(Ivys)
>>> print('Univs', Univs)
Univs [['MIT', 'Cal Tech'], ['Harvard', 'Yale', 'Brown']]
>>> for e in Univs:
	print('e', e)

	
e ['MIT', 'Cal Tech']
e ['Harvard', 'Yale', 'Brown']
>>> for e in Univs:
	print('e=',e)

	
e= ['MIT', 'Cal Tech']
e= ['Harvard', 'Yale', 'Brown']
>>> OnSundaymornings=['goingforarun','goingtothegym','goingforawalk']
>>> print(OnSundaymornings.count('goingforarun'))
1
>>> 
>>> OnSundaymornings.append('playing a musical instrument')
>>> OnSundaymornings
['goingforarun', 'goingtothegym', 'goingforawalk', 'playing a musical instrument']
>>> OnSundaymornings.insert(1,'going to the cinema')
>>> OnSundaymornings
['goingforarun', 'going to the cinema', 'goingtothegym', 'goingforawalk', 'playing a musical instrument']
>>> OnSundaymornings.extend(Techs)
>>> OnSundaymornings
['goingforarun', 'going to the cinema', 'goingtothegym', 'goingforawalk', 'playing a musical instrument', 'MIT', 'Cal Tech']
>>> OnSundaymornings.remove('MIT')
>>> OnSundaymornings
['goingforarun', 'going to the cinema', 'goingtothegym', 'goingforawalk', 'playing a musical instrument', 'Cal Tech']
>>> OnSundaymornings.pop()
'Cal Tech'
>>> OnSundaymornings.pop(2)
'goingtothegym'
>>> OnSundaymornigs.pop(3)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    OnSundaymornigs.pop(3)
NameError: name 'OnSundaymornigs' is not defined
>>> OnSundaymornings(3)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    OnSundaymornings(3)
TypeError: 'list' object is not callable
>>> OnSundaymornings.pop(3)
'playing a musical instrument'
>>> OnSundaymornings
['goingforarun', 'going to the cinema', 'goingforawalk']
>>> OnSundaymornings.pop(2)
'goingforawalk'
>>> OnSundaymornings
['goingforarun', 'going to the cinema']
>>> OnSundaymornings.pop(2)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    OnSundaymornings.pop(2)
IndexError: pop index out of range
>>> OnSundaymornings.pop(1)
'going to the cinema'
>>> OnSundaymornings
['goingforarun']
>>> inagoodmood
[['angry', 'nervous', 'worried'], [...]]
>>> inagoodmood.reverse()
>>> inagoodmood
[[...], ['angry', 'nervous', 'worried']]
>>> Techs
['MIT', 'Cal Tech']
>>> Techs.reverse()
>>> Techs
['Cal Tech', 'MIT']
>>> OnSundaymornings
['goingforarun']
>>> OnSundaymornings.reverse()
>>> OnSundaymornings
['goingforarun']
>>> Techs
['Cal Tech', 'MIT']
>>> Techs.sort()
>>> Techs
['Cal Tech', 'MIT']
>>> Techs.index('MIT')
1
>>> Techs.index('Cal Tech')
0
>>> 
