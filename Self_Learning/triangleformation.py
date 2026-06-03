# program to check whether three sides form a triangle or not

side1 = float(input("Enter the first side: "))
# validate side 1
if(side1 <= 0):
    exit("Side must be positive")

# -------------------------------------------

side2 = float(input("Enter the second side: "))
# validate side 2
if(side2 <= 0):
    exit("Side must be positive")

# -------------------------------------------

side3 = float(input("Enter the third side: "))
# validate side 3
if(side3 <= 0):
    exit("Side must be positive")

# -------------------------------------------

# verifying triangle formation

if(side1 + side2 > side3 and
   side2 + side3 > side1 and
   side1 + side3 > side2):
    print("Above sides form a triangle")
else:
    print("Above sides do not form a triangle")