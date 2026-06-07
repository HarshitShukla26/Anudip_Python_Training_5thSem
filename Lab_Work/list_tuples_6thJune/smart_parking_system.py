#Program for smart parking system
slots = [1, 0, 1, 1, 0, 0, 1, 0]

#TASK 1: Count occupied and available slots
occupied_count = 0
available_count = 0

for slot in slots:
    if slot == 1:
        occupied_count+=1
    else:
        available_count+=1

print("Occupied slots:", occupied_count)
print("Available slots:", available_count)

#TASK 2: Find the first available slot
for i in range(len(slots)):
    if slots[i]==0:
        print("First available slot",i)
        break

#TASK 3:Display all available slot numbers
print("Available slot numbers:")
for i in range(len(slots)):
    if slots[i]==0:
        print(i)

#TASK 4:Check if occupancy exceeds 75%
occupancy = (occupied_count/ len(slots)) * 100

print("Occupancy Percentage:", occupancy)
if occupancy > 75:
    print("Occupancy exceeds 75%")
else:
    print("Occupancy does not exceed 75%")