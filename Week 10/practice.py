def convert_score(score):
    """this function converts a students score (out of 100) into a grade (Fail, Pass, Credit).
        the simple rules are
        if the score is less than 50 then fail
        between 50 and 64 then pass
        over 65 credit
    """
    if score < 0 : 
        return("Error")
    elif score < 50:
        return("Fail")
    elif score <= 64:
        return("Pass")
    else:
        return("Credit")
    
def test_convert_score(score, output):
    if convert_score(score) == output:
        print("YES")
    else:
        print("NO")

def test_all():
    test_convert_score(55, "Pass")
    test_convert_score(49, "Fail")
    test_convert_score(50, "Pass")
    test_convert_score(69, "Credit")
    test_convert_score(-1, "Error")
    test_convert_score(1231241421, "Credit")

test_all()