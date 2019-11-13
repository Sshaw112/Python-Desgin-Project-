#exploring gradient color
from ShawFunction import*
turtle.colormode(255)
bob.speed(0)
turtle.bgcolor("black")
bob.width(1)
#exploring use of r,g,b color values
for times in range(255):
    bob.color(255-times,1,120)
    bob.forward(times*1)
    bob.left(200)
bob.penup()
bob.goto(0,0)
bob.pendown()
for times in range(59):
    bob.color(255-times,1,120)
    bob.forward(times*1)
    bob.left(500)
bob.penup()
bob.goto(-200,200)
bob.pendown()
for times in range(162):
    bob.color(255-times,1,120)
    bob.forward(times*1)
    bob.left(100)
bob.penup()
bob.goto(200,200)
bob.pendown()
for times in range(162):
    bob.color(255-times,1,120)
    bob.forward(times*1)
    bob.left(100)


bob.penup()
bob.goto(-200,-200)
bob.pendown()
for times in range(162):
    bob.color(255-times,1,120)
    bob.forward(times*1)
    bob.left(100)

bob.penup()
bob.goto(200,-200)
bob.pendown()
for times in range(162):
    bob.color(255-times,1,120)
    bob.forward(times*1)
    bob.left(100)

bob.penup()
bob.goto(300,-300)
bob.pendown()
for times in range(56):
    bob.color(255-times,1,120)
    bob.forward(times*1)
    bob.left(1000)

bob.penup()
bob.goto(-300,-300)
bob.pendown()
for times in range(56):
    bob.color(255-times,1,120)
    bob.forward(times*1)
    bob.left(1000)

bob.penup()
bob.goto(-300,300)
bob.pendown()
for times in range(56):
    bob.color(255-times,1,120)
    bob.forward(times*1)
    bob.left(1000)

bob.penup()
bob.goto(300,300)
bob.pendown()
for times in range(56):
    bob.color(255-times,1,120)
    bob.forward(times*1)
    bob.left(1000)

bob.penup()
bob.goto(0,-300)
bob.pendown()
for times in range(162):
    bob.color(255-times,1,120)
    bob.forward(times*1)
    bob.left(92)

bob.penup()
bob.goto(0,300)
bob.pendown()
for times in range(162):
    bob.color(255-times,1,120)
    bob.forward(times*1)
    bob.left(92)

bob.penup()
bob.goto(300,0)
bob.pendown()
for times in range(162):
    bob.color(255-times,1,120)
    bob.forward(times*1)
    bob.left(92)
bob.penup()
bob.goto(-300,0)
bob.pendown()
for times in range(162):
    bob.color(255-times,1,120)
    bob.forward(times*1)
    bob.left(92)

