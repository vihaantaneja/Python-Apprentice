
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""

... # Your code here
#import turtle                           # Tell Python we want to work with the turtle
#turtle.setup (width=600, height=600)    # Set the size of the window

#tina = turtle.Turtle()                  # Create a turtle named tina

#tina.shape('turtle')                    # Set the shape of the turtle to a turtle
#tina.speed(0)                
#for i in range(5):
#    tina.fd(100)
#    tina.lt(360/5)
import turtle                           
turtle.setup (width=500, height=500)    #
tina = turtle.Turtle() 
tina.speed(0)
tina.goto(100,0)
for i in range (10000):
    tina.color("purple")
    tina.backward(100.1)
    tina.circle(100)
    tina.color("red")
    tina.fd(100)              
    tina.circle(100)
    tina.color("blue")
    tina.backward(100.1)
    tina.circle(100)
    tina.color("green")
    tina.fd(100)
    tina.circle(100)
turtle.exitonclick()     