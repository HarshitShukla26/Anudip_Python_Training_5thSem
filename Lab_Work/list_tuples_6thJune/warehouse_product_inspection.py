# List of products
products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

# Display failed product IDs
print("Failed Product IDs:")

pass_count = 0
fail_count = 0

for product in products:
    if product[1] == "Fail":
        print(product[0])
        fail_count += 1
    else:
        pass_count += 1

# Count passed and failed products
print("\nPassed Products:", pass_count)
print("Failed Products:", fail_count)

# Calculate pass percentage
pass_percentage = (pass_count / len(products)) * 100

print("\nPass Percentage:", pass_percentage, "%")

# Stop checking if 3 failures are found
failures = 0

for product in products:
    if product[1] == "Fail":
        failures += 1

    if failures == 3:
        print("\n3 Failures Found. Stopping Check.")
        break
else:
    print("\nLess than 3 Failures Found.")