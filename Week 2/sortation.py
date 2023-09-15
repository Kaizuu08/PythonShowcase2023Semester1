while True:
    number = int(input("your number? (enter 0 to exit) :"))
    
    if number == 0:
        break # exit the while loop if the user enters 0
    
    even_number = False
    odd_number = False

    if number % 2 == 0:
        even_number = True
    else:
        odd_number = True

    if even_number:
        print("your number is even")
    elif odd_number:
        print("your number is odd")
