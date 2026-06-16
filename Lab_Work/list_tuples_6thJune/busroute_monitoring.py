# Passenger count at each stop
passengers = [12, 18, 25, 30, 28, 15, 8]

# Find busiest stop
highest = passengers[0]
stop_number = 1

for i in range(len(passengers)):
    if passengers[i] > highest:
        highest = passengers[i]
        stop_number = i + 1

print("Busiest Stop:", stop_number)
print("Passengers:", highest)

# Display stops with fewer than 10 passengers
print("\nStops With Fewer Than 10 Passengers:")

for i in range(len(passengers)):
    if passengers[i] < 10:
        print("Stop", i + 1, "-", passengers[i])

# Calculate average passengers
total = 0

for p in passengers:
    total += p

average = total / len(passengers)

print("\nAverage Passengers:", average)

# Check whether any stop exceeded 25 passengers
found = False

for p in passengers:
    if p > 25:
        found = True
        break

if found:
    print("\nA stop exceeded 25 passengers.")
else:
    print("\nNo stop exceeded 25 passengers.")