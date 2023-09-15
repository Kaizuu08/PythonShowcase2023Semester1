Mnm = {"red":5,"green":2,"blue":9,"yellow":4}

colour = input("What colour would you like to check?: ")
if colour == "red" or colour == "green" or colour == "blue" or colour == "yellow":
    print(Mnm[colour])
else:
    print("invalid input")

