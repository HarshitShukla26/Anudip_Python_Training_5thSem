#program to simulate an ATM machine
balance = 10000

while (True):
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if (choice == 1):
        print("Current Balance:", balance)

    elif (choice == 2):
        amount = float(input("Enter amount to deposit: "))
        balance = balance + amount
        print(amount, "deposited successfully.")

    elif (choice == 3):
        amount = float(input("Enter amount to withdraw: "))

        if (amount <= balance):
            balance = balance - amount
            print(amount, "withdrawn successfully.")
        else:
            print("Insufficient balance.")

    elif (choice == 4):
        print("EXIT")
        break

    else:
        print("Invalid choice")