from turtle import*

pen1 = Pen()
pen2 = Pen()

pen1.screen.bgcolor('#FF73FF')


pen1.color('red')
pen2.color('yellow')

pen1.forward(100)
pen2.backward(100)

pen1.up()
pen1.goto(-10, 10)
pen1.down()

pen1.begin_fill()
pen1.circle(10)
pen1.end_fill()

pen2.circle(60, -180)
#move the pen
pen1.up()
pen1.goto(100,200)
pen1.down()
#fill a shape(triangle)
pen1.begin_fill()
for i in range(3):
    pen1.forward(750)
    pen1.right(360/3)
pen1.end_fill()
# 20-sided polygon
pen2.begin_fill()
for i in range(20):
    pen2.bk(45)
    pen2.left(360/20)
pen2.end_fill()
    
