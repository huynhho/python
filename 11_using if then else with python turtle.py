from turtle import*
import random

title('Marking an area')
setup(500, 500, 0,0)
bgcolor('white')

delay(0)

for x in range(1,100):
    hoan = random.randint(-250, 250)
    han = random.randint(-250, 250)
    goto(hoan, han)
    print(hoan, han)
    if hoan<50 and han<50:
        print(hoan, 'is less than 50', han)
        dot(20, 'red')
    else:
        dot(20, 'yellow')

done()
