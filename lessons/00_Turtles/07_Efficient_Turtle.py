"""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(0)                           # Make the turtle move as fast, but not too fast. 

def draw_polygon(sides):    
    angle = 360/sides        
    tina.fd(100)
    tina.lt(angle)
for i in range():               
    draw_polygon(123)                        # Draw a hexagon


turtle.done                    # Close the window when we click on it
