"""
This program generates crazy poems, using simple noun and verb phrases.
"""

#This is the dictionary for both nouns and verb phrases
nouns = {0: "The big dog", 1: "The Scaredy Cat", 2: "The Squeaky mouse"}
verbs = {0: "runs", 1: "jumps", 2: "hops", 3: "skips"}

def noun_phrase(number):
    '''Takes in a number and returns a noun phrase'''
    return nouns.get(number % len(nouns))

def verb_phrase(number):
    '''takes in a number and returns a verb phrase'''
    return verbs.get(number % len(verbs))

def line(n1, v1, n2):
    """Generates one line of crazy poetry."""
    print(noun_phrase(n1), verb_phrase(v1), noun_phrase(n2))

def poem(lines):
    """Generates a crazy poem with 'lines' lines."""
    for i in range(0, lines):
        line(i, i + 1, 7 - i)

poem(4)
