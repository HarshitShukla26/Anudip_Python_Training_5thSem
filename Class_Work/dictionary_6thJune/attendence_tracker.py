#Program to create Create Attendance tracker of 30 students.
attendance = {}
for roll in range(1, 31):
    print("Enter attendance of Roll No", roll, "(P/A): ")
    status = input()

    attendance[roll] = status

print("Present Students:")

for roll in attendance:
    if attendance[roll]=="P" or attendance[roll]=="p":
        print(roll)