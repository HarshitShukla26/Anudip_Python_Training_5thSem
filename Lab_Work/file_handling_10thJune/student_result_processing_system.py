#Program for student result processing system
import os

os.chdir(os.path.dirname(__file__))

FILE_NAME="results.txt"


def load_students():
    students=[]

    file=open(FILE_NAME, "r")

    for line in file:
        line=line.strip()

        if line!="":
            data=line.split(",")

            students.append([data[0], data[1], int(data[2])])

    file.close()

    return students


def display_students():
    students=load_students()

    print("Student Records")

    for student in students:
        print(student[0],student[1],student[2])


def search_student():
    sid=input("Enter Student ID : ")

    students=load_students()

    found=False

    for student in students:
        if student[0]==sid:
            print("Student Found")
            print("ID :",student[0])
            print("Name :",student[1])
            print("Marks :",student[2])
            found=True

    if found==False:
        print("Student Not Found")


def topper_lowest():
    students=load_students()

    topper=students[0]
    lowest=students[0]

    for student in students:

        if student[2]>topper[2]:
            topper=student

        if student[2]<lowest[2]:
            lowest=student

    print("Topper")
    print(topper[0],topper[1],topper[2])

    print("Lowest Scorer")
    print(lowest[0],lowest[1],lowest[2])


def class_average():
    students=load_students()

    total=0

    for student in students:
        total=total+student[2]

    avg=total/len(students)

    print("Class Average =",avg)


def pass_fail_count():
    students=load_students()

    pass_count=0
    fail_count=0

    for student in students:

        if student[2]>=40:
            pass_count=pass_count+1
        else:
            fail_count=fail_count+1

    print("Pass Students =",pass_count)
    print("Fail Students =",fail_count)


def generate_grades():
    students=load_students()

    file=open("grades.txt", "w")

    print("Grade Report")

    for student in students:

        marks=student[2]

        if marks>=90:
            grade="A"

        elif marks>=75:
            grade="B"

        elif marks>=40:
            grade="C"

        else:
            grade="F"

        print(student[0],student[1],marks,grade)

        file.write(student[0]+student[1]+grade)

    file.close()

    print("Grades written to grades.txt")


while True:

    print("===== Student Result Management System =====")
    print("1. Display All Students")
    print("2. Search Student by ID")
    print("3. Find Topper and Lowest Scorer")
    print("4. Calculate Class Average")
    print("5. Count Pass and Fail Students")
    print("6. Generate Grades")
    print("7. Exit")

    choice=input("Enter Choice : ")

    if choice=="1":
        display_students()

    elif choice=="2":
        search_student()

    elif choice=="3":
        topper_lowest()

    elif choice=="4":
        class_average()

    elif choice == "5":
        pass_fail_count()

    elif choice=="6":
        generate_grades()

    elif choice=="7":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")