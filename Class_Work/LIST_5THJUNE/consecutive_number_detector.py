numbers = [4, 5, 6, 10, 11, 15, 16, 17]

print("Consecutive pairs:")

for i in range(len(numbers) - 1):
    if numbers[i + 1] - numbers[i] == 1:
        print(numbers[i], numbers[i + 1])