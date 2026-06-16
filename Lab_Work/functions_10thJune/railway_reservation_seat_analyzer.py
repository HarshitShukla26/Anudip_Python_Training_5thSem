#Program for railway reservation seat analyzer
seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]

# Count booked and available seats
def count_seats(seats):
    booked=seats.count("Booked")
    available=seats.count("Available")
    print("Booked Seats =",booked)
    print("Available Seats =",available)

# First available seat
def first_available(seats):
    for i in range(len(seats)):
        if seats[i]=="Available":
            print("First Available Seat =",i+1)
            return

# Occupancy percentage
def occupancy_percentage(seats):
    booked=seats.count("Booked")
    percentage=(booked / len(seats)) * 100
    print("Occupancy Percentage =",percentage, "%")

# Display available seat numbers
def display_available_seats(seats):
    print("Available Seat Numbers:")
    for i in range(len(seats)):
        if seats[i]=="Available":
            print(i+1)
    print()

# Display booked seat numbers
def display_booked_seats(seats):
    print("Booked Seat Numbers:")
    for i in range(len(seats)):
        if seats[i]=="Booked":
            print(i+1)
    print()


count_seats(seats)
first_available(seats)
occupancy_percentage(seats)
display_available_seats(seats)
display_booked_seats(seats)