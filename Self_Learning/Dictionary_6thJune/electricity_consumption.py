#Program for electricity consumption report
units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

#TASK 1: Houses consuming more than 300 units
print("Houses consuming more than 300 units:")
for house in units:
    if units[house]>300:
        print(house)

#TASK 2: Count houses consuming less than 200 units
count=0
for house in units:
    if units[house]<200:
        count+=1

print("Houses consuming less than 200 units",count)

#TASK 3: Find house with highest consumption
for house in units:
    highest_house=house
    highest_units=units[house]
    break

for house in units:
    if units[house]>highest_units:
        highest_units=units[house]
        highest_house=house

print("House with highest consumption:", highest_house)

#TASK 4: Create a list of houses eligible for awareness campaign
campaign=[]
for house in units:
    if units[house]>400:
        campaign.append(house)

print("Houses eligible for awareness campaign:")
print(campaign)

#TASK 5: Categorize houses
print("\House Categories")

for house in units:
    if units[house]<200:
        category="Low"
    elif units[house]<=350:
        category="Medium"
    else:
        category="High"

    print(house,"-",category)