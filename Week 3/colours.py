#Duc Nguyen
#15/02/2023
#This code draws 3 shapes, square, triangle and a hexagon with a variety of colour fill and colour outlined +
#pen size changed

import turtle          # Allows us to use turtles
alex = turtle.Turtle() # Create a turtle, assign to alex
wn = turtle.Screen()   # create a window for our design

#begins drawing the square with colour fill
alex.begin_fill() #starts colour fill
alex.fillcolor("SeaGreen1") #selects colour
for side in range(4): 
        alex.forward(100)
        alex.left(90)
alex.end_fill() #ends fill

#begins drawing the triangle with colour fill
alex.begin_fill() #starts colour fill
alex.fillcolor("SeaGreen2") #selects colour
for side in range(3):
        alex.forward(100)
        alex.left(120)
alex.end_fill() #ends fill

#begins drawing the Hexagon with thick lines & coloured lines
alex.pencolor("SeaGreen3") #pen colour change
alex.pensize(5) #pen thickness change
for side in range(6):
        alex.forward(100)
        alex.left(60)

wn.exitonclick()		  # get rid of the screen. Last step
