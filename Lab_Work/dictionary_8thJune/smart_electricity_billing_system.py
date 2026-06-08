#Program for smart electricity billing system
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

#TASK 1. Display houses consuming more than 400 units
print("Houses consuming more than 400 units:")
for house in units:
    if units[house]>400:
        print(house)

#TASK 2. Find the highest-consuming house
dict_items=list(units.items())

highest_house=dict_items[0][0]
highest_units=dict_items[0][1]

for item in dict_items:
    if item[1]>highest_units:
        highest_house = item[0]
        highest_units = item[1]

print("Highest-consuming house:", highest_house)

#TASK 3. Find the lowest-consuming house
lowest_house=dict_items[0][0]
lowest_units=dict_items[0][1]

for item in dict_items:
    if item[1]<lowest_units:
        lowest_house=item[0]
        lowest_units=item[1]

print("Lowest-consuming house:",lowest_house)

#TASK 4. Calculate total units consumed
total_units=0
for house in units:
    total_units+=units[house]

print("Total units consumed:",total_units)

#TASK 5. Create lists
low=[]
medium=[]
high=[]
for house in units:
    if units[house]<200:
        low.append(house)
    elif units[house]<=400:
        medium.append(house)
    else:
        high.append(house)

print("Low Consumption:",low)
print("Medium Consumption:",medium)
print("High Consumption:",high)

#TASK 6. Count houses eligible for an energy-saving campaign
count=0

for house in units:
    if units[house]>300:
        count+=1

print("Houses eligible for energy-saving campaign:",count)