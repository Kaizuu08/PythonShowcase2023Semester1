'''This code randomises the question asked and determines an output depending on what is entered as an answer
there is a problem as the during the process it determines what answer for the question is, the dictionary may not have a key for it leading to an error
say it asks for "what's your name" and you enter 'yes'. It will try and find a key in the 0 slot of the dictionary that is non-existent
if there is a good input before the bad then good is read first instead of printing 2 answers
if there are no yes,good,bad,no input then it randomises the answer
it is succeptiple to capitalisation of the inputs to questions
'''

import random

Chatbox = {
    "What's your name?": ["Thats a great name"],
    "Are you an ICT112 Student?": ["Thats great","You should try the course!"],
    "Do you like Python?": ["Thats good", "thats not good"],
    "What do you think of turtle graphical interface?": ["yeah i like it too", "yeah i dont like it too"],
    "Do you enjoy programming?":["Thats good I enjoy it too!","Thats not good, I enjoy it though..."],
    "What's your favourite colour?":["mine is red", "mine is blue","mine is yellow","mine is pink","mine is black"],
    "What do you think of the integration of AI":["Interesting, I think its a great way to assist in learning", "Yeah, we should be concerned about the improper use of AI"],
    "Andrew is a pretty cool dont you think?" :["Yeah great Teacher!", "um wrong answer"],
    "What do you think of diversity?":["Yes i agree, diversity can allow us to enhance our knowledge through perspective","I do not agree, diversity is a good thing"],
    "Do you like to write pseudocode or use flowchart?":["yeah writing pseudocode can be a little confusing","flow charts are great graphical representation"]
}

#stores the dictionary and it's keys into questions
questions = list(Chatbox.keys())
# Randomize the order of the questions
random.shuffle(questions)

# Loop through the questions
for question in questions:
    #stores the input into answer
    answer = input(question + " ")
    #detects yes or good in answer input to give relative response
    if 'yes' in answer or 'good' in answer:
        response = Chatbox[question][0]
     #detects no or bad in answer input to give relative response
    elif 'no' in answer or 'bad' in answer:
        response = Chatbox[question][1]
    #detects pseudo or flow to determine the relative response
    elif 'pseudocode' in answer:
        response = Chatbox[question][0]
    elif 'flowchart' in answer:
        response = Chatbox[question][1]
    #if no detection simply chooses a random seletion for reponse
    else:
        response = random.choice(Chatbox[question])

    print(response)

print("That's all the questions for today. Thanks for answering :)")