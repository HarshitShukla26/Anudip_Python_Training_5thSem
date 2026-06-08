#WAP to input a sentence from user and count the number of special charaters present in the sentence
sentence=input("enter a string")
count=0
for ch in sentence:
    if ch.isalnum()==False:
        count+=1

print("the numeber of special characters are ",count)