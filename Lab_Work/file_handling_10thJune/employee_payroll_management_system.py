#Program for employee payroll management system
import os

os.chdir(os.path.dirname(__file__))
FILE_NAME="employees.txt"

def load_employees():
    employees=[]

    file=open(FILE_NAME, "r")

    for line in file:
        data=line.strip().split(",")

        emp={}
        emp["id"]=data[0]
        emp["name"]=data[1]
        emp["salary"]=int(data[2])

        employees.append(emp)

    file.close()

    return employees


def display_employees():
    employees=load_employees()

    print("Employee Records")
    print("----------------------------")

    for emp in employees:
        print(emp["id"],emp["name"],emp["salary"])


def search_employee():
    emp_id=input("Enter Employee ID : ")

    employees=load_employees()

    found=False

    for emp in employees:
        if emp["id"]==emp_id:
            print("Employee Found")
            print("ID :",emp["id"])
            print("Name :",emp["name"])
            print("Salary :",emp["salary"])
            found=True
            break

    if found==False:
        print("Employee Not Found")


def average_salary():
    employees=load_employees()

    total=0

    for emp in employees:
        total=total+emp["salary"]

    average=total/len(employees)

    print("Average Salary =",average)


def highest_lowest_salary():
    employees=load_employees()

    highest=employees[0]
    lowest=employees[0]

    for emp in employees:

        if emp["salary"]>highest["salary"]:
            highest=emp

        if emp["salary"]<lowest["salary"]:
            lowest=emp

    print("Highest Paid Employee")
    print(highest["id"],highest["name"],highest["salary"])

    print("Lowest Paid Employee")
    print(lowest["id"],lowest["name"],lowest["salary"])


def employees_above_50000():
    employees=load_employees()

    print("Employees Earning Above 50000")
    print("-----------------------------")

    for emp in employees:
        if emp["salary"]>50000:
            print(emp["id"],emp["name"],emp["salary"])


def add_employee():
    emp_id=input("Enter Employee ID : ")
    name=input("Enter Employee Name : ")
    salary=input("Enter Salary : ")

    file=open(FILE_NAME, "a")

    file.write(emp_id+name+salary)

    file.close()

    print("Employee Added Successfully")


def salary_categories():
    employees=load_employees()

    print("HIGH CATEGORY")
    for emp in employees:
        if emp["salary"]>=60000:
            print(emp["id"],emp["name"],emp["salary"])

    print("MEDIUM CATEGORY")
    for emp in employees:
        if emp["salary"]>=40000 and emp["salary"]<60000:
            print(emp["id"],emp["name"],emp["salary"])

    print("LOW CATEGORY")
    for emp in employees:
        if emp["salary"]<40000:
            print(emp["id"],emp["name"],emp["salary"])


while True:

    print("===== Employee Payroll Management System =====")
    print("1. Display All Employee Records")
    print("2. Search Employee by ID")
    print("3. Calculate Average Salary")
    print("4. Highest and Lowest Paid Employee")
    print("5. Employees Earning Above 50000")
    print("6. Add New Employee")
    print("7. Generate Salary Categories")
    print("8. Exit")

    choice=input("Enter Your Choice : ")

    if choice=="1":
        display_employees()

    elif choice=="2":
        search_employee()

    elif choice=="3":
        average_salary()

    elif choice=="4":
        highest_lowest_salary()

    elif choice=="5":
        employees_above_50000()

    elif choice=="6":
        add_employee()

    elif choice=="7":
        salary_categories()

    elif choice=="8":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")