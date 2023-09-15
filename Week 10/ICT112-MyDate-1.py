'''This program contains various functions to help with working with dates'''


def isLeapYear(year):
    # returns true or false
    #To be a leap year, the year number must be divisible by four – except for end-of-century years, 
    #which must be divisible by 400. This means that the year 2000 was a leap year, although 1900 was not.

    if (year % 4 == 0):
        # years divisible by 4 are leap unless they are a century, except centuries divisble by 400
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        return True

    return False


def daysInMonth(month, year):
	# returns an int
    # if it's february check if it should be a leap year)
    if (month == 2):
        if (isLeapYear(year)):
            return 29
        else:
            return 28
    elif (month in {4,6,9,11}):
        # checks for April, June, September and November
        return 30
    else:
        # all the rest have 31
        return 31


# Method to test the Days in Month Method
# params: the test year, the test month, the expectd output
def testCaseDaysInMonth(testYear, testMonth, expectedDays):
    afterDays = daysInMonth(testMonth, testYear)
    if (afterDays == expectedDays):
        print("PASSED")
        return True
    else:
        print("FAILED: incorrect days returned. Expected: ", expectedDays, " returned ", afterDays)
        return False


# Test code for DaysInMonth
print("March 2023:", daysInMonth(2023, 3))
result = testCaseDaysInMonth (2021,3,31)

# Add other test cases to thoroughly test the daysInMonth function