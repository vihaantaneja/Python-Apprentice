""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle as turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
import turtle

def set_turtle_image(turtle, image_name):


    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

# Set up the screen

tina = turtle.Turtle()                  # Create a turtle named tina
tina.penup()
tina.goto(0,-100)
tina.shape('arrow')                    # Set the shape of the turtle to a turtle
tina.speed(0)                           # Make the turtle move as fast, but not too fast. 
tina.pensize(50)
tina.pendown()
set_turtle_image(tina,"leaguebot_bolt.gif")
def draw_polygon(sides,size):    
    for i in range(sides):
        tina.pencolor("blue")
        angle = 360/sides        
        tina.fd(size)
        tina.lt(angle)
draw_polygon(6,100)
turtle.done()      
... # Your Code Here