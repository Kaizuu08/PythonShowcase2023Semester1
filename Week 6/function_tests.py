#!/usr/bin/env python
# coding: utf-8

__author__ = 'utting'
import math
import sys


# 1. Write a function called 'rect_area' to calculate the area of a rectangle.
#    Your function should take two inputs: width and height.
#


def rect_area(width, height):
    '''this function calculates the area of a rectangle by taking the width and height and multiplying'''
    area = width*height
    return area



# 2. Write a function called 'rect_perimeter' to calculate the length of
#    the edge of a rectangle.  It should take two inputs: width and height.
#

def rect_perimeter(width, height):
    '''this function calculates the perimeter of a rectangle adding the multiplied by 2, width and height.'''
    perim = width*2+height*2
    return perim



# 3. Write a function called 'postage' that takes the weight of a letter
#    as input (in grams) and returns the postage cost in dollars.
#    We will use the simplified formula that if the letter weighs 250g or less,
#    then the postage is $1.00, but if it weighs more then the postage is $3.50.
#
    
def postage(weight):
    '''this function takes the weight of a letter and returns the postage cost'''
    if weight <= 250:
        cost = 1.00
    else:
        cost = 3.50
    return cost

# 4. Write a function called 'roof_height' calculates the height of a house roof
#    at different positions across the house.  The edges of the house are
#    positioned at x=0 and x=10 metres, and the roof is 3 metres high there.
#    Your function should take a single input (x) and return the height.
#
#    Example:   roof_height(10.0) should return 3.0 (metres).
#
#    From x=0 to x=5 metres, the roof slopes smoothly up to a peak of 6m high,
#    so the roof height formula will be: 3.0 + x * (6.0 - 3.0) / 5.0
#
#    From x=5 to x=10 metres, the roof slopes gradually down again, to 3m high,
#    so the roof height formula will be: 3.0 + (10 - x) * (6.0 - 3.0) / 5.0
#
#    At any other x position (outside 0..10m) there is no roof, so a height
#    of zero metres should be returned.  Here is a rough picture.
#
#         /\     <--- six metres high
#        /  \
#       /    \
#       ------    <--- three metres high
#       |    |
#     __|    |_______
#       0m   10m  20m...
#
def roof_height(x):
    '''Takes in the the house edge at x position and returns the height of the roof'''
    #only run if between 0 and 10
    if x >= 0 and x <= 10:
        #if between 0 and 5
        if x >= 0 and x <= 5:
            height = 3.0 + x * (6.0 - 3.0) / 5.0
        #if between 5 and 10
        elif x > 5 and x <= 10:
            height = 3.0 + (10 - x) * (6.0 - 3.0) / 5.0
    #if outside 0 and 10 height return zero
    else:
        height = 0
    return height

# 5. Write a function called 'fact' that calculates the factorial
#    of its input value, n.  That is, 1 * 2 * 3 * ... * n.
#
#    Hint: you can do this with a loop from 1 up to n - use range(1,n+1),
#    plus a 'result' variable that stores the answer so far.
#
#    This is an example of the 'accumulator' pattern described in the
#    Interactive Python textbook (Functions Chapter).
#


def fact(n):
    '''this function calculates the factorial of a number input value'''
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 6. Write a function called 'count_words' that counts the number of words
#    in a list that have a given length.  For example: count_words(words, 3)
#    should return the number of three-letter words in the list words.
#
#    Hint: this also uses the 'accumulator' pattern, but with a counter
#    variable that we just increment each time we find a good match.
#

def count_words(words, length):
    '''function that counts the words in a list that is == to the length '''
    counter = 0
    for word in words:
        if len(word) == length:
            counter = counter + 1
    return counter


# =====================================================================
# Ignore everything past here.
# These are the helper functions for the unit tests.
# =====================================================================
score = 0

def assert_equals(expected, actual, epsilon=0.001):
    """Checks that the expected and actual values are equal.  Complains if they are not."""
    global score
    line_num = sys._getframe(1).f_lineno
    if expected == actual:
        print("  passed test at line " + str(line_num) + " with " + str(actual) + "  :-)",
              file=sys.stderr)
        score += 1
    elif isinstance(expected, float) and abs(expected - actual) < epsilon:
        print("  passed approximate test at line " + str(line_num) + " with " + str(actual) + "  ;-)",
              file=sys.stderr)
        score += 1
    else:
        print("ERROR: test at line " + str(line_num) + " failed.  Expected "
              + str(expected) + " but got " + str(actual) + "  :-(",
              file=sys.stderr)


def is_documented(func):
    global score
    if func.__doc__ is None:
        print("ERROR: function " + func.__name__ + " is not documented.  :-(",
              file=sys.stderr)
    else:
        print("  Function " + func.__name__ + " is documented.  :-)\n",
              file=sys.stderr)
        score += 1


# =======================================================
# These are the unit tests for each of the functions.
# =======================================================

def test_rect_area():
    """Tests the rect_area(width,height) function."""
    area2 = rect_area(2, 3)
    assert_equals(6, area2)
    area3 = rect_area(5.2, 3.0)
    assert_equals(15.6, area3)
    is_documented(rect_area)


def test_rect_perimeter():
    """Tests the rect_perimeter(width, height) function."""
    assert_equals(14, rect_perimeter(2, 5))
    assert_equals(16.6, rect_perimeter(5.2, 3.1))
    is_documented(rect_perimeter)


def test_postage():
    """Tests the postage(weight) function."""
    assert_equals(1.0, postage(83))
    assert_equals(1.0, postage(250))
    assert_equals(3.5, postage(251))
    assert_equals(3.5, postage(500))
    is_documented(postage)


def test_roof_height():
    """Tests the roof_height(x) function."""
    assert_equals(3.0, roof_height(0))
    assert_equals(3.6, roof_height(1))
    assert_equals(4.8, roof_height(3.0))
    assert_equals(6.0, roof_height(5.0))
    assert_equals(3.0, roof_height(10))
    # now test outside the house region.
    assert_equals(0.0, roof_height(-1))
    assert_equals(0.0, roof_height(10.1))
    is_documented(roof_height)


def test_fact():
    """Tests the fact(n), that is, 'factorial', function."""
    assert_equals(1, fact(1))
    assert_equals(6, fact(3))
    assert_equals(120, fact(5))
    assert_equals(265252859812191058636308480000000, fact(30))
    assert_equals(1, fact(0))
    is_documented(fact)


def test_count_words():
    """Tests the count_words function."""
    assert_equals(1, count_words(["The", "race", "is", "over"], 2))
    assert_equals(2, count_words(["The", "race", "is", "over"], 4))
    assert_equals(3, count_words(["why", "not", "me", "too"], 3))
    assert_equals(0, count_words([], 1))
    is_documented(count_words)


def test_all():
    """Unit tests all the functions in this file."""
    global score
    score = 0
    try:
        print("Testing rect_area...", file=sys.stderr)
        test_rect_area()
        print("Testing rect_perimeter...", file=sys.stderr)
        test_rect_perimeter()
        print("Testing postage...", file=sys.stderr)
        test_postage()
        print("Testing roof_height...", file=sys.stderr)
        test_roof_height()
        print("Testing fact...", file=sys.stderr)
        test_fact()
        print("Testing count_words...", file=sys.stderr)
        test_count_words()
    except NameError as err:
        print("Error:", err)
    print("You passed", score, "tests!")

# Execute this each time you want to test all your functions.
# See how many smiley faces you can get...
# (it is normal to get an error at the end if you have not written all 6 functions yet)
test_all()





