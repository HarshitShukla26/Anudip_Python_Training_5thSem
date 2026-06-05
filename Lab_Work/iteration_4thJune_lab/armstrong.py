# Program to check if a number is an Armstrong number
num = int(input("Enter a number: "))

temp = num
count = 0

# Count digits
while (temp > 0):
    count = count + 1
    temp = temp // 10

temp = num
sum = 0

# Calculate sum of digits raised to count
while (temp > 0):
    digit = temp % 10
    sum = sum + digit ** count
    temp = temp // 10

if (sum == num):
    print(num, "is an Armstrong Number")
else:
    print(num, "is Not an Armstrong Number")