#program to calculate simple interest
#input the values
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (years): "))
#-----------------------------------------------

#validate the input
if (principal <= 0):
    exit("Principal should be greaer than 0")
#-------------------------
elif (rate < 0):
     exit("Rate cannot be negative")
#-------------------------
elif (time <= 0):
    exit(" Time must be greater than 0")
#-------------------------
#displaying the interest
else:
    si = (principal * rate * time) / 100
    print("Simple Interest =", si)