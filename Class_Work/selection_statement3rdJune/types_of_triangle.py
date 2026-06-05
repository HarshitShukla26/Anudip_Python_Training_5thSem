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
    #triangle is formed
    #acute angled triangle
    if(angle1<90 and angle2<90 and angle3<90):
        print("acute angled triangle")
    #right angled triangle
    elif(angle1==90 or angle2==90 or angle3==90):
        print("right angled triangle")
    #obtuse angled triangle
    else:
        print("obtuse angled triangle")
else:
    print("above angles do not form a triangle")