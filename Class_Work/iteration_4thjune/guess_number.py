#a program that repeatedly asks the user to guess the number and displays a success message when the correct number is entered

secret_numnber=7
guess=int(input("Guess the number"))

while(guess!=secret_numnber):
    print("Wrong guess")
    guess=int(input("Guess the number"))

print("Correct guess")