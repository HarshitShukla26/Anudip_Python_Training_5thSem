#prgram to remove duplicate entries from a list
#creating  blank list to store numbers
numbers=[]
for i in range(20):
    num=int(input("enter the number"))
    #append into list
    numbers.append(num)

x = int(input("Enter the number to remove from the list: "))
#--------------------------------------------------------------
#finding the frequency of the given number
frequency=numbers.count(x)
if frequency==0:
    print("element not found")
elif frequency==1:
    print("no duplicates found")
else:
    #reversing the list
    numbers.reverse()
    for i in range(1,frequency):
        numbers.remove(x)
    #reversing the list again
    numbers.reverse()
    print("list after removing duplicates",numbers)