#Program for daily expense tracker and report generator
import os
os.chdir(os.path.dirname(__file__))

FILE_NAME="expenses.txt"


def load_expenses():

    expenses=[]

    file=open(FILE_NAME, "r")

    for line in file:

        line=line.strip()

        if line!="":

            data=line.split(",")

            expenses.append([data[0],data[1]])

    file.close()

    return expenses


def save_expenses(expenses):

    file=open(FILE_NAME, "w")

    for expense in expenses:

         file.write(expense[0]+expense[1])
    file.close()


def display_expenses():

    expenses=load_expenses()

    print("All Expenses")

    for expense in expenses:

        print(expense[0],expense[1])


def total_expenditure():

    expenses=load_expenses()

    total=0

    for expense in expenses:

        total=total+int(expense[1])

    print("Total Expenditure =",total)


def highest_lowest():

    expenses=load_expenses()

    highest=expenses[0]
    lowest=expenses[0]

    for expense in expenses:

        if int(expense[1])>int(highest[1]):
            highest=expense

        if int(expense[1])<int(lowest[1]):
            lowest=expense

    print("Highest Expense")
    print(highest[0], highest[1])

    print("Lowest Expense")
    print(lowest[0], lowest[1])


def expenses_above_800():

    expenses=load_expenses()

    print("Expenses Greater Than 800")

    for expense in expenses:

        if int(expense[1])>800:

            print(expense[0],expense[1])


def add_expense():

    category=input("Enter Category : ")
    amount=input("Enter Amount : ")

    expenses=load_expenses()

    expenses.append([category,amount])

    save_expenses(expenses)

    print("Expense Added Successfully")


def update_expense():

    category=input("Enter Category : ")

    expenses=load_expenses()

    found=False

    for expense in expenses:

        if expense[0].lower()==category.lower():

            amount=input("Enter New Amount : ")

            expense[1]=amount

            save_expenses(expenses)

            print("Expense Updated Successfully")

            found=True

            break

    if found==False:

        print("Category Not Found")


def generate_report():

    expenses=load_expenses()

    total=0

    highest=expenses[0]
    lowest=expenses[0]

    for expense in expenses:

        total=total+int(expense[1])

        if int(expense[1])>int(highest[1]):
            highest = expense

        if int(expense[1])<int(lowest[1]):
            lowest=expense

    file = open("report.txt", "w")

    file.write("SUMMARY REPORT\n\n")

    file.write("Highest Expense Category : ")
    file.write(highest[0])
    file.write("\n")

    file.write("Lowest Expense Category : ")
    file.write(lowest[0])
    file.write("\n\n")

    file.write("Categories Spending More Than 800\n")

    for expense in expenses:

        if int(expense[1])>800:

            file.write(expense[0])
            file.write(" ")
            file.write(expense[1])
            file.write("\n")

    file.close()

    print("Report Generated Successfully")


while True:

    print("===== Expense Tracker =====")
    print("1. Display All Expenses")
    print("2. Calculate Total Expenditure")
    print("3. Highest and Lowest Expense")
    print("4. Expenses Greater Than 800")
    print("5. Add New Expense")
    print("6. Update Expense")
    print("7. Generate Report")
    print("8. Exit")

    choice = input("Enter Choice : ")

    if choice=="1":
        display_expenses()

    elif choice=="2":
        total_expenditure()

    elif choice=="3":
        highest_lowest()

    elif choice=="4":
        expenses_above_800()

    elif choice=="5":
        add_expense()

    elif choice=="6":
        update_expense()

    elif choice=="7":
        generate_report()

    elif choice=="8":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")