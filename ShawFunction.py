#function file
import turtle
bob = turtle.Turtle()

def square(distance):
    for times in range(4):
        bob.square(100)
        bob.right(90)


def star(d,c):
    bob.color(c)
    for times in range(5):
        bob.forward(d)
        bob.right(144)

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown() 

def explosion(d,c):
    bob.color(c)
    bob.begin_fills()
    for times in range(8):
        bob.forward(d)
        bob.right(135)
        bob.end_fill()


def polygon(sides,distance,c):
    angle = 360/sides
    bob.color(c)
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.right(angle)
    bob.end_fill()  



def portal():
    for times in range(60):
        c =(times*4,times*4,times*4)#r,g,b
