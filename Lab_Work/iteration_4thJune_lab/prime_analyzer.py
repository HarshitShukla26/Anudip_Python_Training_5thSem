count = 0
num = int(input("Enter a number: "))

if num <= 1:
    print("Number should be greater than 1")
else:
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
        print("Factors are:")
        for i in range(1, num + 1):
            if num % i == 0:
                print(i)