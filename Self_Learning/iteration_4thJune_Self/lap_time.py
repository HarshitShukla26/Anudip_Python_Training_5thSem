# This program takes the lap times of racers, identifies the fastest and slowest racers, and calculates the difference in their lap times.
n = int(input("Enter number of racers: "))

for i in range(1, n + 1):
    print("Enter lap time of racer", i)
    lap_time = int(input())

    if (i == 1):
        fastest = lap_time
        slowest = lap_time
        fastest_pos = 1
        slowest_pos = 1
    else:
        if (lap_time < fastest):
            fastest = lap_time
            fastest_pos = i

        if (lap_time > slowest):
            slowest = lap_time
            slowest_pos = i

difference = slowest - fastest

print("Fastest Racer Position:", fastest_pos)
print("Slowest Racer Position:", slowest_pos)
print("Difference in Lap Time:", difference)