# Program to check if a number is a palindrome or not
num = int(input("Enter a number: "))

temp = num
reverse = 0

while (temp > 0):
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if (num == reverse):
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")