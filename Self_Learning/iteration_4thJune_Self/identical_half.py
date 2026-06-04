# This program checks if the first and last halves of a number are identical.
num = int(input("Enter a number: "))

temp = num
count = 0

while (temp > 0):
    count += 1
    temp = temp // 10

if (count % 2 != 0):
    print("Number must have even digits")
else:
    half = count // 2

    divisor = 1

    for i in range(half):
        divisor = divisor * 10

    left_half = num // divisor
    right_half = num % divisor

    if (left_half == right_half):
        print("Both halves are identical")
    else:
        print("Both halves are not identical")