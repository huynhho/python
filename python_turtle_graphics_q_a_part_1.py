from turtle import*
import time
pen1 = Pen()
pen2 = Pen()

pen1.color('black', 'green')
pen2.color('red', 'yellow')

pen1.up()
pen1.goto(0, 100)
pen1.down()
pen1.write('hello', False, 'center',font=('Cooper Black', 18, 'bold'))

# pause for 2 seconds
time.sleep(3)
pen1.clear()
pen1.write('class', True, 'left', font=('Cambria', 22, 'bold'))
help(pen1.write)

