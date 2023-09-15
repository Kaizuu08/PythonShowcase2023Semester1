# A class of students with first name, last name, student number, task 1-2-3 scores
class ICT112_Student:
    def __init__(self,first_name,last_name,student_number, list_dbl_task_1 ,dbl_task_2, dbl_task_3):
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number
        self.list_dbl_task_1 = list_dbl_task_1
        self.dbl_task_2 = dbl_task_2
        self.dbl_task_3 = dbl_task_3


# method to get the student number
    def get_student_num(self):
        print(self.student_number)

#method to set the student number
    def set_student_num(self, student_number):
        self.student_number = student_number
        print("Student Number set to: " + str(student_number))


# method to get the task 1 score with errors checks
    def get_task_1_total(self):

    # Sort the list in descending order
        self.list_dbl_task_1 = sorted(self.list_dbl_task_1, reverse=True)
        
        # iterating through the list
        for i, score in enumerate(self.list_dbl_task_1[:8]):
            # if the list contains >5 or <0 returns an error
            if score > 5 or score < 0:
                print("Error: task 1 score too high or too low: score at double " + str(i + 1) + " is " + str(score))
                break  # exit loop if invalid score is found

            #checks if the task 1 list has 8 submissions otherwise returns error
            elif len(self.list_dbl_task_1) <8 or len(self.list_dbl_task_1) >8:
                print("Task 1 does not have 8 submissions")
                break # exit loop if task 1 is invalid list

        else:  # if loop finishes normally
            six_highest_num = self.list_dbl_task_1[:6]
            total = sum(six_highest_num)
            print("This student scored " + str(total) + " on their six highest scores.")

    def get_all(self):
        print(self.first_name)
        print(self.last_name)
        print(self.student_number)

        for i, score in enumerate(self.list_dbl_task_1[:8]):
            # if the list contains >5 or <0 returns an error
            if score > 5 or score < 0:
                print("Error: task 1 score too high or too low: score at double " + str(i + 1) + " is " + str(score))
                break  # exit loop if invalid score is found

            #checks if the task 1 list has 8 submissions otherwise returns error
            elif len(self.list_dbl_task_1) >8:
                print("Task 1 has over 8 submissions?")
                break # exit loop if task 1 is invalid list

            self.list_dbl_task_1 = sorted(self.list_dbl_task_1, reverse=True)
            six_highest_num = self.list_dbl_task_1[:6]
            total = sum(six_highest_num) + self.dbl_task_2 + self.dbl_task_3
            if total >= 85:
                print ("High Distinctions: " + str(total))
            elif total > 84 and total >= 75:
                print ("Distinction: " + str(total))
            elif total > 74 and total >= 65:
                print ("Credit: " + str(total))
            elif total > 64 and total >= 50:
                print ("Pass: " + str(total))
            else:
                print("failure: " + str(total))
            return
#################################################################

# list of students
students = [
    ICT112_Student("John","Doe","123456",[4.0, 3.5, 5.0, 5.0, 4.5, 5.0, 5.0, 4.0], 40, 35.5), #normal
    ICT112_Student("impossibly","dumb","654321",[-1.0, -5.0, 0, 0, 0, 0, 0, 0], 0, 0), #Test negative index & grade
    ICT112_Student("Get","Wong","99999",[5.0, 3.5, 5.0, 5.0,5.0,5.0,5.0, 6.0], 40, 40), #test over index
    ICT112_Student("Lebronny","James","123451",[4.0, 2.5, 4.0, 2.0, 3.5, 1.0, 5.0, 2.0], 12, 15), #normal test grade
    ICT112_Student("Hoe","Hingle","58283",[5.0, 3.5, 5.0, 5.0,5.0,5.0,5.0, 1.0], 40, 40), #test normal
    ICT112_Student("explode","bruh","58283",[3.5, 5.0, 5.0,4.0], 40, 40), #test below submissions
    ICT112_Student("explode","bruh","58283",[3.5, 5.0, 5.0, 4.0, 3.5, 5.0, 5.0, 4.0, 4.0], 40, 40) #test below submissions
]

# tests
students[0].get_student_num()
students[0].get_task_1_total()

students[1].set_student_num(21321321321)

students[2].get_task_1_total()

for student in students:
    student.get_all()
    # student.get_student_num()
    # student.set_student_num(123456)
    # student.get_task_1_total()
