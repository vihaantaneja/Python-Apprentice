"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 

tina.pensize(30)
colors = [ 'red', 'orange', 'green', 'blue']    # define a list of colors

for color in colors:                            # loop through the colors
    tina.pencolor(color)
    tina.fd(100)
    tina.lt(90)
# 2) Make another square, but put the colors in reverse order, using a negative index. 

... # Your code here

turtle.done()                     # Close the window when we click on it