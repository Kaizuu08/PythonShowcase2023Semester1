#Duc Nguyen
#15/03/2023
#Draws a spirograph with added fill colour and white pen lines


import turtle          # Allows us to use turtles
alex = turtle.Turtle() # Create a turtle, assign to alex
wn = turtle.Screen()   # create a window for our design


# a Python program to draw circles/spirals
alex.reset() #resets the turtles values to original
alex.speed(100) #makes alex the turtle faster
alex.pencolor("white") #pen colour
alex.begin_fill()  #fill
alex.fillcolor("SeaGreen2") #fill colour
for i in range(36):  #spirograph
    alex.forward(100)
    alex.left(10)
    alex.forward(100)
    alex.left(120)
alex.end_fill() #finish fill


wn.exitonclick()		  # get rid of the screen. Last step
