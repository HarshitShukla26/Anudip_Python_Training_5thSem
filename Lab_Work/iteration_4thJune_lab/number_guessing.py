#generating a random number between 1 and 50
number=int(input("Enter a number between 1 and 50: "))

while(number>1 or number<50):
    guess=int(input("enter your guess "))

    if(guess<number):
        print("Too low")
    elif(guess>number):
        print("Too high")
    else:
        print("correct guess")
        break