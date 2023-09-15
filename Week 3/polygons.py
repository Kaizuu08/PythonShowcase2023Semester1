#Duc Nguyen
#15/03/2023
#This program takes the input of a string although you have to type exactly the string for it to activate, after typing
#the selected strings a shape will be printed by alex the turtle. The program then finishes and windows may be closed

import turtle          # Allows us to use turtles
alex = turtle.Turtle() # Create a turtle, assign to alex
wn = turtle.Screen()   # create a window for our design

shape = input("What shape? square, rectangle, triangle, hexagon: ")

if shape == "square":
    for side in range(4):
        alex.forward(100)
        alex.left(90)

elif shape == "rectangle":
    for side in range(2):
        alex.forward(50) 
        alex.left(90)       
        alex.forward(30) 
        alex.left(90) 


elif shape == "triangle":
    for side in range(3):
        alex.forward(100)
        alex.left(120)

elif shape == "hexagon":            #This is the main assessment
    for side in range(6):
        alex.forward(100)
        alex.left(60)



wn.exitonclick()		  # get rid of the screen. Last step
