#Program for employee performance dashboard
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

#TASK 1. Display employees scoring above 80
print("Employees scoring above 80:")
for emp in performance:
    if performance[emp]>80:
        print(emp)

#TASK 2. Count employees needing improvement
count=0
for emp in performance:
    if performance[emp]<60:
        count+=1

print("Employees needing improvement:",count)

#TASK 3. Find the top performer
dict_items=list(performance.items())

top_perfomer=dict_items[0][0]
top_score=dict_items[0][1]

for item in dict_items:
    if item[1]>top_score:
        top_perfomer=item[0]
        top_score=item[1]

print("Top Performer:",top_perfomer)

#TASK 4. Calculate average performance score
total=0
for emp in performance:
    total+=performance[emp]

average=total/len(performance)
print("Average Performance Score:",average)

#TASK 5. Create separate lists
excellent=[]
good=[]
average_list=[]
poor=[]

for emp in performance:
    if performance[emp] >= 90:
        excellent.append(emp)
    elif performance[emp] >= 75:
        good.append(emp)
    elif performance[emp] >= 60:
        average_list.append(emp)
    else:
        poor.append(emp)

print("Excellent:",excellent)
print("Good:",good)
print("Average:",average_list)
print("Poor:",poor)