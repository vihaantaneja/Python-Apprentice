"""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""


import random
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["red", "blue", "green", "yellow", "orange"]


def getNextColor(i):
    return colors[i % len(colors)]
tina = turtle.Turtle()                  # Create a turtle named tina
tina.penup()
tina.goto(0,-100)
tina.shape('arrow')                    # Set the shape of the turtle to a turtle
tina.speed(0)                           # Make the turtle move as fast, but not too fast. 
tina.pensize(50)
tina.pendown()
def draw_polygon(sides,size):    
    for i in range(sides):
        tina.pencolor(getRandomColor())
        angle = 360/sides        
        tina.fd(size)
        tina.lt(angle)
z = 10
x = 50
y = 100
for i in range(10):
    draw_polygon(z,y)
    y = y - 15
    z = z - 1                    # Draw a hexagon
    x = x - 5
    tina.pensize(x)
tina.hideturtle()
turtle.done()                    # Close the window when we click on it
