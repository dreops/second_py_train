#Excercise: print grade based on marks with use of functions.
#Print: Stud. name, grades for Homework(/25), Assessment(/50),
# Final Exam(/100)

#getting the input and assigning the variables
stud_name           = (input("What is your name? "))
homework_score      = int(input("Enter homework score out of 25 "))
assessment_score    = int(input("Enter assessment score out of 50 "))
exam_score          = int(input("Enter exam score out of 100 "))

def total_grade(homework_score, assessment_score, exam_score):
    grade = homework_score + assessment_score + exam_score
    return grade

#NameError in the above the name 'grade is not defined'

ICT_grade = total_grade

print(stud_name , grade)

