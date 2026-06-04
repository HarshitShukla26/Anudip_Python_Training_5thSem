# This program finds the length of the longest increasing sequence in a series of numbers entered by the user.
n = int(input("Enter how many numbers: "))

longest = 1
current = 1

prev = int(input("Enter number: "))

for i in range(2, n + 1):
    num = int(input("Enter number: "))

    if (num > prev):
        current += 1
    else:
        current = 1

    if (current > longest):
        longest = current

    prev = num

print("Length of longest increasing sequence:", longest)