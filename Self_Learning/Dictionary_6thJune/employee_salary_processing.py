#Program for employee salary processing
salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

#TASK 1: Employees earning above 60000
print("Employees earning above 60000:")
for emp in salary:
    if salary[emp]>60000:
        print(emp)

#TASK 2: Count employees earning below 40000
count=0
for emp in salary:
    if salary[emp]<40000:
        count += 1

print("Employees earning below 40000",count)

#TASK 3: Find highest paid employee
for emp in salary:
    highest_emp=emp
    highest_salary=salary[emp]
    break

for emp in salary:
    if salary[emp]>highest_salary:
        highest_salary=salary[emp]
        highest_emp=emp

print("Highest-paid employee:",highest_emp)

#TASK 4: Create a list for employees eligible for bonus
bonus=[]
for emp in salary:
    if salary[emp]>50000:
        bonus.append(emp)

print("Employees eligible for bonus")
print(bonus)

#TASK 5: Calculate average salary
total = 0
for emp in salary:
    total+=salary[emp]

average=total/len(salary)
print("Average Salary",average)