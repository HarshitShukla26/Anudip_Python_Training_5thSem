# This program calculates the electricity bill based on the units consumed and applies a surcharge if the bill exceeds ₹5000.
units = int(input("Enter electricity units consumed: "))

if (units>0 and units<=100):
    bill = units * 5

elif (units>100 and units<=200):
    bill = units * 7

elif(units>200):
    bill = units * 10

if(bill > 5000):
    surcharge = bill * 10 / 100
    bill = bill + surcharge

print("Final Payable Amount:", bill)