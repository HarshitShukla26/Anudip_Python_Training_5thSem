sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

#TASK 1. Display products sold more than 20 times
print("Products sold more than 20 times:")
for product in sales:
    if sales[product] > 20:
        print(product)

#TASK 2. Find the best-selling product
dict_items = list(sales.items())

best_product = dict_items[0][0]
highest_sales = dict_items[0][1]

for item in dict_items:
    if item[1] > highest_sales:
        best_product = item[0]
        highest_sales = item[1]

print("Best-selling product:", best_product)
print("Sales:", highest_sales)

#TASK 3. Find the least-selling product
least_product = dict_items[0][0]
lowest_sales = dict_items[0][1]

for item in dict_items:
    if item[1] < lowest_sales:
        least_product = item[0]
        lowest_sales = item[1]

print("Least-selling product:", least_product)
print("Sales:", lowest_sales)

#TASK 4. Calculate total products sold
total = 0

for product in sales:
    total += sales[product]

print("Total products sold:", total)

#TASK 5. Create a list of products requiring promotion
promotion = []

for product in sales:
    if sales[product] < 15:
        promotion.append(product)

print("Products requiring promotion:", promotion)

#TASK 6. Count products having sales between 10 and 30
count = 0

for product in sales:
    if sales[product] >= 10 and sales[product] <= 30:
        count += 1

print("Products with sales between 10 and 30:", count)