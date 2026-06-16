#Program for food delivery performance tracker
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# 1. Fastest delivery
def fastest_delivery(times):
    return min(times)

# 2. Delayed orders
def delayed_orders(times):
    delayed=[]
    for time in times:
        if time>45:
            delayed.append(time)
    return delayed

# 3. Average delivery time
def average_delivery_time(times):
    return sum(times)/len(times)

# 4. Delivery category
def delivery_category(times):
    for i in range(len(times)):
        if times[i]<=30:
            category="Fast"
        elif times[i]<=45:
            category="Normal"
        else:
            category="Delayed"

        print("Order", i+1, ":", times[i], "minutes ->",category)


# Function Calls
print("Fastest Delivery Time =",fastest_delivery(delivery_time), "minutes")

print("Delayed Orders =",delayed_orders(delivery_time))

print("Average Delivery Time =",average_delivery_time(delivery_time), "minutes")

print("Delivery Categories:")
delivery_category(delivery_time)