#Program for employee salary processing
employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

#TASK 1: Display employees earning above 50000
print("Employees earning above 50000:")
for employee in employees:
    if employee[1]>50000:
        print(employee[0])

#TASK 2: Find highest-paid employee
highest = employees[0]

for employee in employees:
    if employee[1]>highest[1]:
        highest=employee

print("Highest paid employee")
print(highest[0])

#TASK 3:Calculate total salary expenditure
total = 0
for employee in employees:
    total+=employee[1]

print("Total salary expenditure",total)

#TASK 4: Count employees earning below 40000
count=0
for employee in employees:
    if employee[1]<40000:
        count+=1

print("Employees earning below 40000",count)