#Program for cricket scoreboard analysis
scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

#TASK 1: Players who scored 50 or more runs
print("Players who scored 50 or more runs")
for player in scores:
    if scores[player]>=50:
        print(player)

#TASK 2: Count centuries
centuries=0
for player in scores:
    if scores[player]>=100:
        centuries+=1

print("Number of centuries",centuries)

#TASK 3: Find highest scorer
for player in scores:
    highest_player=player
    highest_score=scores[player]
    break

for player in scores:
    if scores[player]>highest_score:
        highest_score=scores[player]
        highest_player=player

print("Highest scorer:", highest_player)

#TASK 4: Create a list of players scoring below 30 runs
below_30=[]
for player in scores:
    if scores[player]<30:
        below_30.append(player)

print("Players scoring below 30 runs")
print(below_30)

#TASK 5: Players scoring between 50 and 99
count = 0
for player in scores:
    if scores[player]>=50 and scores[player]<=99:
        coun +=1

print("Players scoring between 50 and 99",count)