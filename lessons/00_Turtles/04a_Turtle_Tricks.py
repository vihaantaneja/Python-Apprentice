import turtle                           
turtle.setup (width=500, height=500)    #
tina = turtle.Turtle() 
tina.speed(0)
tina.goto(-100,0)
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
