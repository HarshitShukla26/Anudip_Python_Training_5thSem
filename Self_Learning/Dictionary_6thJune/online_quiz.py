#Program for online quiz performance
quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

#TASK 1: Students scoring 15 or above
print("Students scoring 15 or above:")
for student in quiz_scores:
    if quiz_scores[student]>=15:
        print(student)

#TASK 2: Count students scoring below 10
count=0
for student in quiz_scores:
    if quiz_scores[student]<10:
        count+=1

print("Students scoring below 10",count)

#TASK 3: Find the top performer
for student in quiz_scores:
    top_student=student
    top_score=quiz_scores[student]
    break

for student in quiz_scores:
    if quiz_scores[student]>top_score:
        top_score=quiz_scores[student]
        top_student=student

print("Top Performer",top_student)

#TASK 4: Create a list of students who passed
passed=[]
for student in quiz_scores:
    if quiz_scores[student]>=10:
        passed.append(student)

print("Students who passed")
print(passed)

#TASK 5: Calculate class average
total=0

for student in quiz_scores:
    total+=quiz_scores[student]

average=total/len(quiz_scores)
print("Class Average",average)