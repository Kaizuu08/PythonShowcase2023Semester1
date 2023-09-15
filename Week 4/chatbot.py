#Duc Nguuen
'''This is a chatbox that determines what is in the input then responds with various
answers and inputs which then repeats till it reach a conclusion and then reset
this code suffers from impractibility
There is a troll towards the conclusion where depending on the input will make a loop repeating an answer
'''

#This may or may not be used later
chatbox = True
while chatbox == True:

    #Question 1
    q1 = input("Hi, I am a chatbox. I would like to ask you some questions, is that okay? ")
    #if Q1 input has yes do this
    if 'yes' in q1:
        q2 = input("Are you an ICT112 Student?: ")
        #if Q2 input has yes do this
        if 'yes' in q2:
            q3 = input("Do you think diversity and incluisity is important? ")
            #if Q3 input has yes do this
            if 'yes' in q3:
                print("That's great because, Diversity and Inclusion are important because they promote creativity, innovation, equality, and respect of different perspectives and experience")
                q4 = input("Do you prefer writing pseudocode or flowcharts? ")
                #if q4 has flowchart do this    
                if 'flowchart' in q4:
                    print("Graphical representations are a great way to show how your code works :)")
                    q5 = input("Did you know that turtles are easier to train than snakes? ")
                    #if yes in q5 do this
                    if 'yes' in q5:
                        print("That's Awesome :), that concludes my questions for today")
                    #if no in q5 do this - this is just a troll causing it to loop forever
                    elif 'no' in q5:
                        loop = True
                        while loop == True:
                            print("You see TURTLES")
                    #do this if q5 is not appropriate input
                    else:
                        print("Oh ok :( )")
                    #if q4 has psuedocode do this
                elif 'pseudocode' in q4:
                    print("I see, although i find that some pesudocode is hard to understand")  
                    q5 = input("Did you know that turtles are easier to train than snakes? ")
                    #if yes in q5 do this
                    if 'yes' in q5:
                        print("That's Awesome :), that concludes my questions for today")
                    #if no in q5 do this- this is just a troll causing it to loop forever
                    elif 'no' in q5:
                        loop = True
                        while loop == True:
                            print("You see TURTLES")
                    #do this if q5 is not appropriate input
                    else:
                        print("Oh ok :( )")
                #do this if Q4 is not appropriate input
                else:
                    print("Oh ok :( )")
            #do this if Q3 is not a yes
            else: 
                print("Oh ok :( )")
    #do this if Q2 is not a yes
        else:
            print("Oh ok :( )")
    #do this if Q1 is not a yes
    else:   
        print("Oh ok :( ")

