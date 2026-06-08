#Program for cricket tournament statistics
runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

#TASK 1. Display players scoring more than 500 runs
print("Players scoring more than 500 runs:")
for player in runs:
    if runs[player]>500:
        print(player)

#TASK 2. Find the Orange Cap winner
dict_items=list(runs.items())

orange_cap=dict_items[0][0]
highest_runs=dict_items[0][1]

for item in dict_items:
    if item[1]>highest_runs:
        orange_cap=item[0]
        highest_runs=item[1]

print("Orange Cap Winner:",orange_cap)
print("Runs:",highest_runs)

#TASK 3. Find the lowest scorer
lowest_scorer=dict_items[0][0]
lowest_runs=dict_items[0][1]

for item in dict_items:
    if item[1]<lowest_runs:
        lowest_scorer=item[0]
        lowest_runs=item[1]

print("Lowest Scorer:",lowest_scorer)

#TASK 4. Calculate total runs scored
total_runs=0
for player in runs:
    total_runs+=runs[player]

print("Total Runs Scored:",total_runs)

#TASK 5. Create a list of players scoring below 400
below_400 = []
for player in runs:
    if runs[player] < 400:
        below_400.append(player)

print("Players scoring below 400:",below_400)

#TASK 6. Count players scoring between 400 and 600 runs
count=0
for player in runs:
    if runs[player] >= 400 and runs[player]<=600:
        count+=1

print("Players scoring between 400 and 600 runs:",count)