#Program for bus route passenger analysis
passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}

#TASK 1: Stops having more than 20 passengers
print("Stops having more than 20 passengers:")
for stop in passengers:
    if passengers[stop]>20:
        print(stop)

#TASK 2: Count stops with fewer than 10 passengers
count=0
for stop in passengers:
    if passengers[stop]<10:
        count+=1

print("Stops with fewer than 10 passengers",count)

#TASK 3: Find the busiest stop
for stop in passengers:
    busiest_stop=stop
    max_passengers=passengers[stop]
    break

for stop in passengers:
    if passengers[stop]>max_passengers:
        max_passengers=passengers[stop]
        busiest_stop=stop

print("Busiest stop",busiest_stop)

#TASK 4: Create a list of stops requiring an extra bus
extra_bus = []
for stop in passengers:
    if passengers[stop]>25:
        extra_bus.append(stop)

print("Stops requiring an extra bus")
print(extra_bus)

#TASK 5: Calculate average number of passengers
total=0
for stop in passengers:
    total+=passengers[stop]

average=total/len(passengers)
print("Average number of passengers",average)