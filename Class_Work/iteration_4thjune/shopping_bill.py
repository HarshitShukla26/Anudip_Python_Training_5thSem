#program that continuously accepts item prices and calculates the total bill.The program should stop accepting prices when the user enters 0
total_bill=0

while(True):
    price=float(input("Enter the price of the item"))
    if(price==0):
        break
    else:
        total_bill+=price
    
print("Total bill:",total_bill)