students = 1
student_present = 0
student_absent = 0

while students <= 30:
    status = input("Is the student present or absent: ").lower()

    if (status == "present"):
        student_present += 1
    elif (status == "absent"):
        student_absent += 1
    else:
        print("Invalid input")

    students += 1

print("Total students present:", student_present)
print("Total students absent:", student_absent)