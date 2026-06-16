#List of passengers
passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

# 1. Display all waiting-list passengers
print("Waiting List Passengers:")

for passenger in passengers:
    if passenger[1] == "Waiting":
        print(passenger[0])

# 2. Count confirmed and waiting passengers
confirmed = 0
waiting = 0

for passenger in passengers:
    if passenger[1] == "Confirmed":
        confirmed += 1
    else:
        waiting += 1

print("\nConfirmed Passengers:", confirmed)
print("Waiting Passengers:", waiting)

# 3. Check whether a specific passenger has a confirmed ticket
name = input("\nEnter passenger name: ")

found = False

for passenger in passengers:
    if passenger[0] == name and passenger[1] == "Confirmed":
        found = True
        break

if found:
    print("Passenger has a Confirmed Ticket")
else:
    print("Passenger does not have a Confirmed Ticket")

# 4. Create separate lists
confirmed_list = []
waiting_list = []

for passenger in passengers:
    if passenger[1] == "Confirmed":
        confirmed_list.append(passenger[0])
    else:
        waiting_list.append(passenger[0])

print("\nConfirmed List:", confirmed_list)
print("Waiting List:", waiting_list)