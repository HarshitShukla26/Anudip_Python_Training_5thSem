# This program checks if a 6-digit code is valid based on the sum of the first three digits and the last three digits.
num = int(input("Enter a 6-digit code: "))

temp = num
count = 0

while (temp > 0):
    count += 1
    temp = temp // 10

if (count != 6):
    print("Invalid Code")
else:
    last3 = num % 1000
    first3 = num // 1000

    sum1 = 0
    sum2 = 0

    while (first3 > 0):
        sum1 += first3 % 10
        first3 = first3 // 10

    while (last3 > 0):
        sum2 += last3 % 10
        last3 = last3 // 10

    if (sum1 == sum2):
        print("Valid Secret Code")
    else:
        print("Invalid Secret Code")