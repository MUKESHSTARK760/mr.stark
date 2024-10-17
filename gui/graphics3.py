import turtle
a=turtle.Turtle()
turtle.bgcolor("white")
a.pensize(10)
a.speed(5)
a.left(90)
a.forward(100)
a.left(220)
a.forward(70)
a.left(95)
a.forward(70)
a.right(135)
a.forward(100)


#u
a.pencolor("blue")
a.pensize(10)
a.penup()
a.goto(250,0)
a.left(390)
a.pendown()
a.right(120)
a.forward(110)
a.circle(60,175)
a.left(5)
a.forward(115)


#k
a.pensize(10)
a.speed(5)
a.left(90)
a.forward(100)
a.backward(50)
a.right(60)
a.forward(80)
a.backward(80)
a.right(60)
a.forward(80)


#e
a.penup()
a.setpos(-50,50)
a.pendown()
a.pensize(20)
a.pencolor("blue")
a.speed(5)
a.forward(100)
a.backward(100)
a.right(90)
a.forward(100)
a.left(90)
a.forward(100)
a.backward(100)
a.right(90)
a.forward(100)
a.left(90)
a.forward(100)
a.done()


#s
turtle.bgcolor("pink")
a.pensize(20)
a.speed(5)
a.pencolor("pink")
a.penup()
a.goto(-480,300)
a.right(26)
a.pendown()
for x in range(100):
    a.backward(1.3)
    a.left(2)
for x in range(100):
    a.backward(1.3)
    a.right(2)

#h
a.pensize(10)
a.speed(5)
a.left(90)
a.forward(100)
a.backward(50)
a.right(90)
a.forward(100)
a.left(90)
a.forward(50)
a.backward(100)



turtle.done()