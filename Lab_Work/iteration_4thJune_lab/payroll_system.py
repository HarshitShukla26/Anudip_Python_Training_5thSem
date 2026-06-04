# Program to calculate gross salary, net salary and grade of an employee
name = input("Enter employee name: ")
basic_salary = int(input("Enter basic salary: "))

hra = basic_salary * 20 / 100
da = basic_salary * 10 / 100
pf = basic_salary * 12 / 100

gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf

print("Employee Name:", name)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)

if (net_salary > 50000):
    print("Grade: Senior Grade")
elif (net_salary > 30000):
    print("Grade: Mid Grade")
else:
    print("Grade: Junior Grade")