#Program for inventory management system
inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

#TASK 1: Products with stock less than 10
print("Products with stock less than 10:")
for product in inventory:
    if inventory[product] < 10:
        print(product)

#TASK 2: Count products having stock more than 50
count = 0
for product in inventory:
    if inventory[product] > 50:
        count += 1

print("Products with stock more than 50", count)

#TASK 3: Find product with minimum stock
for product in inventory:
    min_product = product
    min_stock = inventory[product]
    break

for product in inventory:
    if inventory[product] < min_stock:
        min_stock = inventory[product]
        min_product = product

print("Product with minimum stock", min_product)

#TASK 4: List of products requiring restocking
restock = []

for product in inventory:
    if inventory[product] < 20:
        restock.append(product)

print("Products requiring restocking:")
print(restock)

#TASK 5: Calculate total inventory count
total = 0
for product in inventory:
    total += inventory[product]

print("Total inventory count", total)