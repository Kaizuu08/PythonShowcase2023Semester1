import turtle          # Allows us to use turtles
alex = turtle.Turtle() # Create a turtle, assign to alex
wn = turtle.Screen()   # create a window for our design

# This draws a snail shell haha
forward = 10
alex.begin_fill() 
alex.fillcolor("SeaGreen2") 
for side in range(10):
        alex.forward(forward)
        alex.left(90)
        forward = forward + 10
alex.end_fill()

wn.exitonclick()		  # get rid of the screen. Last step
