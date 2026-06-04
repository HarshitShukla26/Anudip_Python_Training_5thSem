# This program checks if the digits of a number are consecutive in decreasing order.
num = int(input("Enter a number: "))

temp = num
prev_digit = temp % 10
temp = temp // 10

flag = True

while (temp > 0):
    digit = temp % 10

    if (prev_digit - digit != 1):
        flag = False
        break

    prev_digit = digit
    temp = temp // 10

if (flag):
    print(num, "follows the pattern")
else:
    print(num, "does not follow the pattern")