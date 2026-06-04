#program for login system
password="admin123"
user_password=input("Enter your password: ")

while(user_password!=password):
    print("Incorrect password. Try again.")
    user_password=input("Enter your password: ")

print("Login successful")