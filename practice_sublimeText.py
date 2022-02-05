x=-9
ans=0
while ans*ans*ans < abs(x):
	ans= ans +1
	print('current guess =', ans)
if ans*ans*ans != abs(x):
		print (x,'is not a perfect cube')
elif x<0:
		ans = -ans
print('Cube root of ' + str(x) + ' is '+ str(ans))
compound_nouns = {'active role','extended family','family gathering','immediate family','maternal instinct'}
print(compound_nouns)
set(range(10))
print (compound_nouns & set(range(10)))
squares = [x**2 for x in range(10)]
print(squares)
skill={i+ 'Hoan' for i in compound_nouns}
print(skill)
social_skills={k + ' "Hoan is handsome" ' for k in compound_nouns}
print(social_skills)
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
print(len('bear in mind'), len('broaden the mind'), len ('have something in mind'), len('have something on your mind'))
print(compound_nouns | social_skills)
a={1,2,3,4,5}
b={1,3,5,7}
print(a|b)
print((a|b) & b)
print((a|b) ^ b)
print(((a|b)^(a|b))|a)
print(True ^ False)
print(True&False)
print(True&False | False)
print(True&False | False| False & True)

x=2
y=4
print(x!=y)
# prints even numbers from 2 to 10
while(x<=10):
	x +=2
	print(x)
for i in (2,4,6,8,10):
	print(i)
a=2
while(a<=10):
	a += 2
	print(a)
cart=[]
print(type(cart))
print('Who is responsible for filing invoices')
print([(m,n) for m in ['The woman is talking to the man','The people are drawing pictures on the street'] for n in ['The man is looking around the buildings','The man is sitting at the stop'] if len(m)<len(n)])
print(len("The woman is talking to the man"), len('The people are drawing pictures on the street'), len("The man is looking around the buildings"))
print('When can I schedule you for an interview')
tupA = (1, 'apple', 6.00)
tupB = (tupA, 'MIT', [4,5])
print('tupA is', tupA, 'with length', len(tupA) )
print('tupB is', tupB,'with length', len(tupB))
print('\nIndexing operations:')
print('tupA[0] is', tupA[0])
print([0]*10)
print([[]]*10)

print('\n Matrix')
M = [[0,1],[1,2],[2,3],[3,4]]
print (M)
print(M[3])
print(M[2])
print(M[2][1])




def increment(n):
	return n+1
def square(n):
	return n**2
def findSequence(initial, goal):
	# construct list of 'candidates' of form ('1 increment increment',3)
	candidates = [(str(initial), initial)]