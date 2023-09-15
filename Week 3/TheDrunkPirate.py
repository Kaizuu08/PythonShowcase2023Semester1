import turtle          # Allows us to use turtles
alex = turtle.Turtle() # Create a turtle, assign to alex
wn = turtle.Screen()   
import random

alex.pencolor("red")
alex.pensize(5) 
for step in range(0,10):
    angle = random.randint(-90,120)
    print("Pirate turns by " + str(angle) + " degrees.") 
    alex.forward(100) 
    alex.left(angle)   

wn.exitonclick()   # get rid of the screen. Last step