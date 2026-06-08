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

# 1. Products sold more than 20 times
print("Products sold more than 20 times:")
for product in sales:
    if sales[product]>20:
        print(product)

#TASK 2: Best selling product
for product in sales:
    max_product=product
    max_sales=sales[product]
    break

for product in sales:
    if sales[product]>max_sales:
        max_sales=sales[product]
        max_product=product

print("Best-selling product",max_product)

#TASK 3: Least-selling product
for product in sales:
    min_product=product
    min_sales=sales[product]
    break

# Find minimum
for product in sales:
    if sales[product]<min_sales:
        min_sales=sales[product]
        min_product=product

print("Least-selling product",min_product)

# TASK 4: Total products sold
total=0
for product in sales:
    total=total+sales[product]

print("Total products sold",total)

# TASK 5: Crate a list of products requiring promotion
promotion=[]
for product in sales:
    if sales[product]<15:
        promotion.append(product)

print("Products requiring promotion:",promotion)

# TASK 6: Count products having sales between 10 and 30
count=0
for product in sales:
    if sales[product]>=10 and sales[product]<=30:
        count=count+1

print("Products with sales between 10 and 30:",count)