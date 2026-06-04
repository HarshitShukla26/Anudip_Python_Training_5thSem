#program to claculate electricity bill
units=int(input("Enter the number of units consumed: "))

if(units>0 and units<=100):
    bill=units*5
    print("Electricity bill is: ",bill,"LOW CONSUMPTION")
elif(units>100 and units<=200):
    bill=units*7
    print("Electricity bill is: ",bill,"MODERATE CONSUMPTION")
elif(units>200):
    bill=units*10
    print("Electricity bill is: ",bill,"HIGH CONSUMPTION")