# This program simulates the movement of a lift in a building and calculates the total floors travelled based on user input for destination floors.
current_floor = 0
total_floors = 0

while (True):
    destination = int(input("Enter destination floor: "))

    if (destination == -1):
        break

    floors_travelled = destination - current_floor

    if (floors_travelled < 0):
        floors_travelled = -floors_travelled

    print("Floors travelled in this trip:", floors_travelled)

    total_floors += floors_travelled
    current_floor = destination

print("Total floors travelled:", total_floors)