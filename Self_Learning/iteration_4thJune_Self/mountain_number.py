# This program checks if a given number is a Mountain Number or not.
num = int(input("Enter a number: "))

# Reverse the number
temp = num
rev = 0

while (temp > 0):
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

increasing = True
decreasing = False

prev = rev % 10
rev = rev // 10

while (rev > 0):
    digit = rev % 10

    if (increasing):
        if (digit > prev):
            prev = digit
        elif (digit < prev):
            increasing = False
            decreasing = True
            prev = digit
        else:
            print("Not a Mountain Number")
            break

    elif (decreasing):
        if (digit < prev):
            prev = digit
        else:
            print("Not a Mountain Number")
            break

    rev = rev // 10
else:
    if (decreasing):
        print("Mountain Number")
    else:
        print("Not a Mountain Number")