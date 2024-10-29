"""
Pentagon Crazy

This program already works. Run it, then change it to make it draw a different pattern.
"""

import random
import turtle

def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

def getNextColor(i):
    return colors[i % len(colors)]

window = turtle.Screen()

window.setup(width=600, height=600, startx=0, starty=0)

colors = (getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor(), getRandomColor())
turtle.bgcolor("black")
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.speed(0)
myTurtle.width(10)
myTurtle.pensize(10)
sides = 5
angle = 360 / sides

for i in range(36000000000000000000000000000000000000):
    if i == 100:
        myTurtle.width(100)
    if i == 200:
        myTurtle.width(3)
    myTurtle.pencolor(getNextColor(i))
    myTurtle.forward(i)
    myTurtle.right(angle + 1)

myTurtle.hideturtle()

turtle.done()
