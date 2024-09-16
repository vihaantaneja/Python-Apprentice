"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
t = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()
t.fd(100)
t.lt(360/5)
t.fd(100)
t.lt(360/5)
t.fd(100)
t.lt(360/5)
t.fd(100)
t.lt(360/5)
t.fd(100)
t.lt(360/5)
... # Your code here

turtle.exitonclick()                    # Close the window when we click on it
