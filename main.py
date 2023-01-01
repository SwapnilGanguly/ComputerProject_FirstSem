from rich.console import Console
from rich.markdown import Markdown

console = Console()
MARKDOWN = """ 
# Welcome to Student Portal 
"""
md = Markdown(MARKDOWN)
console.print(md)

while(True):
    print("Student operations - 1")
    print("Course operations - 2")
    print("Batch operations - 3")
    print("Department operations - 4")
    print("Examination operations - 5")
    print("Terminate - 0")
    x = int(input("Enter your choice: "))
    if(x == 0):
        break
    elif(x == 1):
        from student import *
        while(True):
            print("Create a student - 1")
            print("Update a student's details - 2")
            print("Remove a student - 3")
            print("Generate report card of a particular student - 4")
            print("Return to main menu - 0")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                student_id = input("Student ID: ")
                student_name = input("Student name: ")
                createStudent(student_id, student_name)
            elif(y == 2):
                ostudent_id = input("Enter old student ID: ")
                updateStudent(ostudent_id)
            elif(y == 3):
                student_id = input("Student ID: ")
                removeStudent(student_id)
            elif(y == 4):
                student_id = input("Student ID: ")
                reportCard(student_id)
            else:
                print("Invalid input. Please try again.")
    elif(x == 2):
        from course import *
        while(True):
            print("Create a course - 1")
            print("View performance of students on a course - 2")
            print("Show course statistics as histogram - 3")
            print("Return to main menu - 0")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                course_id = input("Course ID: ")
                course_name = input("Course name: ")
                createCourse(course_id, course_name)
            elif(y == 2):
                course_id = input("Course ID: ")
                checkPerformance(course_id)
            elif(y == 3):
                student_id = input("Course ID: ")
                courseStatistics(course_id)
            else:
                print("Invalid input. Please try again.")
    elif(x == 3):
        from batch import *
        while(True):
            print("Create a batch - 1")
            print("View all students in a particular batch - 2")
            print("Show all courses in a batch - 3")
            print("View performance of all students in a batch - 4")
            print("View pie chart of percentage all students in a batch - 5")
            print("Return to main menu - 0")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                batch_name = input("Batch name: ")
                createBatch(batch_name)
            elif(y == 2):
                batch_id = input("Batch ID: ")
                viewStudents(batch_id)
            elif(y == 3):
                batch_id = input("Batch ID: ")
                viewCourses(batch_id)
            elif(y == 4):
                batch_id = input("Batch ID: ")
                viewPerformance(batch_id)
            elif(y == 5):
                batch_id = input("Batch ID: ")
                pieChart(batch_id)
            else:
                print("Invalid input. Please try again.")
    elif(x == 4):
        from department import *
        while(True):
            print("Create a department - 1")
            print("View all batches in a department - 2")
            print("View average performance of all batches in a department - 3")
            print("View line plot of department statistics - 4")
            print("Return to main menu - 0")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                department_id = input("Department ID: ")
                department_name = input("Department name: ")
                createDepartment(department_id, department_name)
            elif(y == 2):
                department_id = input("Department ID: ")
                viewBatches(department_id)
            elif(y == 3):
                department_id = input("Department ID: ")
                viewPerformanceD(department_id)
            elif(y == 4):
                department_id = input("Department ID: ")
                linePlot(department_id)
            else:
                print("Invalid input. Please try again.")
    elif(x == 5):
        from examination import *
        while(True):
            print("Enter marks of all students for an exam - 1")
            print("View performance of all students in an exam - 2")
            print("Show examination statistics as a scatter plot - 3")
            print("Return to main menu - 0")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                course_id = input("Course ID: ")
                enterMarks(course_id)
            elif(y == 2):
                course_id = input("Course ID: ")
                viewPerformanceE(course_id)
            elif(y == 3):
                scatterPlot()
            else:
                print("Invalid input. Please try again.")
    else:
        print("Invalid input. Please try again.")
