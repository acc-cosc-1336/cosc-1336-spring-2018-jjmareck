#write the import statements to bring in homework 4 functions
#valid_letter_grade, get_credit_points, get_grade_points, and get_grade_point_average
from src.homework.homework4 import valid_letter_grade
from src.homework.homework4 import get_credit_points
from src.homework.homework4 import get_grade_points
from src.homework.homework4 import get_grade_point_average
'''
Use the functions from homework4 to...
Write code to prompt the user for number of students and grades.
Create a nested loop to collect letter grades and credit hours for each student.
Vaidate the letter grade is in accepted range if not prompt user for letter again.
From the letter grade, get the credit points for that class.
Calculate grade points (How? Research GPA calculation).
Sum grade points and credit hours for each student.
Calculate GPA for each student.
Display Student 1(etc) GPA is 3.77. Format the GPA to two values.
'''

#WRITE YOUR CODE IN THE MAIN FUNCTION BELOW
def main():
    num_students = int(input('Number of students... '))
    num_grades = int(input('Number of grades... '))
    gpa = 0;
    for student_index in range(num_students):
        total_credit_hours = 0;
        total_grade_points = 0;
        for grades_index in range(num_grades):
            valid = False
            while not valid:
                letter_grade = input('Enter letter grade '+str(grades_index+1)+' for student#' + str(student_index+1) + '... ')
                valid = valid_letter_grade(letter_grade)

            credit_hours = int(input('Enter credit hours '+str(grades_index+1)+' for student#' + str(student_index+1) + '... '))

            credit_points = get_credit_points(letter_grade)
            grade_points = get_grade_points(credit_hours, credit_points)
            total_credit_hours += credit_hours
            total_grade_points += grade_points

        gpa = get_grade_point_average(total_credit_hours, total_grade_points)
        print('Student ' + str(student_index+1) + ' GPA is ' + str(gpa))

        


#CALL THE MAIN FUNCTION


main()
