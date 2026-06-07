#program for e commerce order analysis
orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

#TASK 1: Display products costing more than 1000
print("products costing more than 1000")
for product in orders:
    if product[1]>1000:
        print(product[0])

#TASK 2: Find the most expensive product
max_product = orders[0]
for product in orders:
    if product[1]>max_product[1]:
        max_product=product

print("Most expensive product")
print(max_product[0])

#TASK 3: Calculate total order value
total=0
for product in orders:
    total+=product[1]

print("Total order value",total)

#TASK 4: Count products costing below 1000
count=0

for product in orders:
    if product[1]<1000:
        count+=1

print("Number of orders below 1000 are",count)