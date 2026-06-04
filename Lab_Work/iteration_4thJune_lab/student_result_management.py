#program to accept the marks of 5 subject and grade them
total=0
fail_count=0

for i in range(1,6):
    print("enter the marks for subjects",i)
    marks=int(input())
    total=total+marks

    if (marks<40):
        fail_count+=1

percentage=total/5

if(percentage>=90):
    print("GRADE A+")
elif(percentage>=75):
    print("GRADE A")
elif(percentage>=60):
    print("GRADE B")
elif(percentage>=40):
    print("GRADE C")
else:
    print("FAIL")

print("Total marks",total)
print("Percentage",percentage)
print("Number of subjects failed",fail_count)