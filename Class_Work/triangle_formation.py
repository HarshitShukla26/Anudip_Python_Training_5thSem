#program to check three angles form a triangle or not
angle1=float(input("eneter the first angle"))
#validate angle 1
if(angle1<=0):
    exit("angle must be positive")
#-------------------------------------------
angle2=float(input("eneter the second angle"))
#validate angle 2
if(angle2<=0):
    exit("angle must be positive")
#-------------------------------------------
angle3=float(input("eneter the third angle"))
#validate angle 3
if(angle3<=0):
    exit("angle must be positive")
#-------------------------------------------
#verifying triangle formation
if(angle1+angle2+angle3==180):
    print("above angles form a triangle")
else:
    print("above angles do not form a triangle")