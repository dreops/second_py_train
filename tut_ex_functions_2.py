#Excercise: print grade based on marks with use of functions.
#Print: Stud. name, grades for Homework(/25), Assessment(/50),
# Final Exam(/100)

#getting the input and assigning the variables
stud_name           = (input("What is your name? "))
homework_score      = int(input("Enter homework score out of 25 "))
assessment_score    = int(input("Enter assessment score out of 50 "))
exam_score          = int(input("Enter exam score out of 100 "))

def avg_calc (homework_score + assessment_score + exam_score):
    

#below is copied from grade.py

score = float (input("Please input score"))
if score >= 70:
    print("Your grade is 1st")
elif score >= 60:
    print("Your grade is 2:1")
elif score >= 50:
    print("Your grade is 2:2")
elif score >= 40:
    print("Your grade is pass")
else:
    print ("Your grade is fail, but don't let anyone ever tell you that you are a failure")

def total_grade(homework_score, assessment_score, exam_score):
    grade = homework_score + assessment_score + exam_score
    return grade

#NameError in the above the name 'grade is not defined'

ICT_grade = total_grade

print(stud_name , grade)

