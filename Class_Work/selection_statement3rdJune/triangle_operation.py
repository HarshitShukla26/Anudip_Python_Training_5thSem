#program to calculate area and perimeter of a triangle
#input of three sides

print("----Triangle-----]")
side1=int(input("Enter the first side of the triangle(in cm): "))
side2=int(input("Enter the second side of the triangle(in cm): "))
side3=int(input("Enter the third side of the triangle(in cm): "))
#---------------------------------------------------------------------
print("--------------------------------------------------------")
print("First Side:", side1, "cm")
print("Second Side:", side2, "cm")
print("Third Side:", side3, "cm")
#to calculate perimeter
perimeter=side1+side2+side3
#---------------------------------------------------------------------

s=perimeter/2

#displaying area

print("area:", (s*(s-side1)*(s-side2)*(s-side3))**0.5, "cm^2")

#displaying perimeter
print("perimeter:", perimeter, "cm")