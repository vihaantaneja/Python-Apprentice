"""

Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Background Image"


Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
"""
import turtle
import random

def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a turtle and set its shape to the custom GIF
     # Tell Python we want to work with the turtle
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
turtle.bgcolor(getRandomColor())
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
set_turtle_image(tina, "pikachu.gif")
tina.penup()
tina.speed(1)

for i in range(100):
    tina.goto(200, 200)
    tina.goto(200, -200)
    tina.goto(-200, -200)
    tina.goto(-200, 200)
tina.goto(0,0)
turtle.done()                    # Close the window when we click on it
   