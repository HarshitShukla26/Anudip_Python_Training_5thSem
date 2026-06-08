sentence=input("enter a string")
count=0
for ch in sentence:
    if ch.isalnum()==False:
        count+=1

print("the numeber of special characters are ",count)