#program that  repeatedly asks the user to enter a PIN until the correct is entered
correct_pin=1234
count=0
user_pin=int(input("Enter your PIN: "))
count+=1

while(user_pin!=correct_pin):
    count+=1
    print("Incorrect PIN. Try again.")
    user_pin=int(input("Enter your PIN: "))

print("PIN verified")
print("Number of attempts:",count)