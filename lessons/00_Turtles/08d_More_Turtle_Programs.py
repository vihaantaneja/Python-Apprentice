


"""this is the pikanado 3.0 ultra
"""
import turtle
import random
a = random.randint(-300, 300)
b = random.randint(-300, 300)

def set_turtle_image(turtle, image_name):


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
    tina.goto(a,b)
    a = random.randint(-300, 300)
    b = random.randint(-300, 300)

tina.goto(0,0)
turtle.done()                    # Close the window when we click on it

# this is the secret moustach jiggle code!
"""import turtle

def set_turtle_image(turtle, image_name):


    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)
def set_background_image(window, image_name):

    from pathlib import Path
    from PIL import Image


    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a turtle and set its shape to the custom GIF
     # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

screen = turtle.Screen()                # Get the screen that tina is on
set_background_image(screen, "emoji.png") # Set the background image of the screen

set_turtle_image(tina, "moustache1.gif")
tina.penup()
tina.speed(1)

for i in range(1000):
    tina.goto(0,-10)
    tina.goto(0,10)
turtle.done()      
... # Your code here
"""
    

