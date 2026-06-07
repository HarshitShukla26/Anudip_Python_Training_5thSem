prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1800,
    "Monitor": 12000,
    "Printer": 9000,
    "Tablet": 28000,
    "Speaker": 3500,
    "Webcam": 2500,
    "Headphones": 4200,
    "Router": 3200
}

#TASK 1: Products costing more than 5000
print("Products costing more than 5000:")
for product in prices:
    if prices[product]>5000:
        print(product)

#TASK 2: Count products costing less than 3000
count=0
for product in prices:
    if prices[product]<3000:
        count+=1

print("Products costing less than 3000",count)

#TASK 3: Find the most expensive product
for product in prices:
    max_product=product
    max_price=prices[product]
    break

for product in prices:
    if prices[product]>max_price:
        max_price=prices[product]
        max_product=product

print("Most expensive product",max_product)

#TASK 4: Create a list of products priced between 2000 and 10000
product_list = []
for product in prices:
    if prices[product]>=2000 and prices[product]<=10000:
        product_list.append(product)

print("Products priced between 2000 and 10000")
print(product_list)

#TASK 5: Calculate total value of all products
total = 0
for product in prices:
    total+=prices[product]

print("Total value of all products",total)