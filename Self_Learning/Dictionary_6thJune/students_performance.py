#Program to track students performance
marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}

#TASK 1: Students scoring 80 or above
print("Students scoring 80 or above:")
for name in marks:
    if marks[name]>=80:
        print(name)

#TASK 2: Count failed students
count = 0
for name in marks:
    if marks[name]<40:
        count+=1

print("Number of failed students are",count)

#TASK 3: Find the highest scorer
for name in marks:
    highest_name = name
    highest_marks = marks[name]
    break

for name in marks:
    if marks[name] > highest_marks:
        highest_marks = marks[name]
        highest_name = name

print("Highest scorer:", highest_name)

#TASK 4: Create a list of students scoring between 60 to 75
students_60_75 = []

for name in marks:
    if marks[name] >= 60 and marks[name] <= 75:
        students_60_75.append(name)

print("Students scoring between 60 and 75 are")
print(students_60_75)

#TASK 5: Assign grades
print("Grades:")
for name in marks:
    if marks[name]>=90:
        grade ="A"
    elif marks[name]>=75:
        grade ="B"
    elif marks[name]>=50:
        grade ="C"
    else:
        grade ="F"

    print(name, "->", grade)