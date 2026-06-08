#Program for city temperature management system
temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

#TASK 1. Display cities having temperature above 40°C
print("Cities having temperature above 40°C:")
for city in temperature:
    if temperature[city]>40:
        print(city)

#TASK 2. Find the hottest city
dict_items=list(temperature.items())

hottest_city=dict_items[0][0]
highest_temp=dict_items[0][1]

for item in dict_items:
    if item[1]>highest_temp:
        hottest_city=item[0]
        highest_temp=item[1]

print("Hottest City:",hottest_city)
print("Temperature:",highest_temp)

#TASK 3. Find the coolest city
coolest_city=dict_items[0][0]
lowest_temp=dict_items[0][1]

for item in dict_items:
    if item[1]<lowest_temp:
        coolest_city=item[0]
        lowest_temp=item[1]

print("Coolest City:",coolest_city)
print("Temperature:",lowest_temp)

#TASK 4. Calculate average temperature
total=0
for city in temperature:
    total+=temperature[city]

average=total/len(temperature)

print("Average Temperature:",average)

#TASK 5. Create a list of pleasant cities (temperature < 35°C)
pleasant=[]
for city in temperature:
    if temperature[city]<35:
        pleasant.append(city)

print("Pleasant Cities:",pleasant)

#TASK 6. Count cities with temperature between 35°C and 40°C
count=0
for city in temperature:
    if temperature[city]>=35 and temperature[city]<=40:
        count+=1

print("Cities with temperature between 35°C and 40°C:",count)