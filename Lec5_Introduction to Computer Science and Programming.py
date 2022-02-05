##L1 = [2]
##L2 =[L1,L1]
##print ('L2=',L2)
##L1[0]=3
##print ('L2=',L2)
##L2[0]= 'a'
##print ('L2=',L2)
##L1 = [2]
##print ('L2=',L2)
##def copyList(LSource, LDest):
##    for e in LSource:
##        LDest.append(e)
##        print ('LDest =', LDest)
##
##L1 =[]
##L2 =[1,2,3]
##copyList(L2,L1)
##print (L1)
##print (L2)
##copyList(L1,L1)
##print (L1)
##print (L1)
##print (L2)
##D = {1: 'one', 'daux': 'two','pi': 3.14159}
##D1=D
##print (D1)
##D[1]='uno'
##print (D1)
##for k in D1.keys():
##    print (k, '=', D1[k])
##
##     
##        
##for k in D1.keys():
##    print (k, '=', D1[k])


##students = {'uta', 'tim', 'yuen'}
##salads ={'green salad', 'fruit salad'}
##main_courses ={'spaghetti','fish'}
##desserts = {'pie','cake'}
##beverages = {'milk','soda','coffee'}
##relation = {'uta': 'pie','tim':'pie' ,'Yuen':'pie'}
##
##for element in students:
##    if element in relation.keys():
##        print(element,'=',relation[element])


##del (EtoF['bread'])
##def keySearch(L,k):
##    for elem in L:
##        if elem[0]==k: return elem[1]
##    return None
##print(keySearch([21,32,4,5],2))
##EtoF = {'bread': 'du pain', 'wine': 'du vin',\
##        'eats': 'mange', 'drinks': 'bois',\
##        'likes': 'alone', 1: 'un',\
##        '6.08': '6.00'}
####print (EtoF)
####print (EtoF.keys())
####print (EtoF.keys)
##del EtoF[1]
##print (EtoF)
##del EtoF['bread']
##print (EtoF)
##def translateWord(word, dictionary):
##    if word in dictionary:
##        return dictionary[word]
##    else:
##        return word
##print(translateWord('eats',EtoF))
##print(translateWord('handsome',EtoF))
##              this is so hard for me to run?????
##def translate(sentence):
##    translation = ''
##    word = ''
##    for c in sentence:
##        if c != '':
##            word = word + c
##        else:
##            translation = translation + ''\
##                          + translateWord(word,EtoF)
##            word = ''
##    return translation[1:] + '' + translateWord(word,EtoF)
##print(translate('John eats bread'))
##print(translate('Steve drinks wine'))
##print(translate('John likes 6.00'))
##
##x = 100
##divisors = ()
##for i in range(1,x):
##    if x% i == 0:
##        divisors = divisors + (i,)
##        print(divisors)
##
##print (divisors)

def toChars(s):
    import string
    s = string.ascii_lowercase(s)
    ans = ''
    for c in s:
        if c in string.ascii_lowercase:
            ans = ans + c
    return ans 
print(toChars(2233))




