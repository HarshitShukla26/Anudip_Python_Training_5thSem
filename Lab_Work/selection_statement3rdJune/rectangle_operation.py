#program to calculate the area and perimeter of a rectangle
#input of length and breadth
length=int(input("Enter the length"))
breadth=int(input("Enter the breadth"))
#-----------------------------------------------

#validate the input
if(length>0 and breadth>0):
    area=length*breadth
    perimeter=2*(length+breadth)
#displaying area and perimeter
    print("Area= ", area)
    print("Perimeter=", perimeter)
#-------------------------
else:
    exit("the input is invalid")