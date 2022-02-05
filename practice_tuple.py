tupA = (1, 'apple', 6.00)
tupB = (tupA, 'MIT', [4,5])
print('tupA is', tupA, 'with length', len(tupA) )
print('tupB is', tupB,'with length', len(tupB))
print('\nIndexing operations:')
print('tupA[0] is', tupA[0])
print('tupA[2] is', tupA[2])
print('tupB[0] is', tupB[0])
print('tupB[0][1] is', tupB[0][1])
print('tupB[-1] is', tupB[-1])
print('tupA[0:1] is', tupA[0:1])
print('tupA[0:2] is', tupA[0:2])
print('tupA[0:3] is', tupA[0:3])
print('tupA[0:4] is', tupA[0:4])
print('tupA[0:100] is', tupA[0:100])
print('tupA[:2] is', tupA[:2])
print('tupA[1:] is', tupA[1:])
print('tupA[:] is', tupA[:])
print('tupB[-1:-3] is', tupB[-1:-3])
print('\nIteration through tup B')
for i in range(len(tupB)):
    print(tupB[i], 'is of type', type(tupB[i]))


print('\n Matrix')
M = [[0,1],[1,2],[2,3],[3,4]]
print (M)



