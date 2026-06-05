#program to convert time into coreesponding hours and minutes and seconds
#input of time in seconds
second=int(input("Enter the time in seconds: "))
#check second is negative
if(second<0):
    exit("time cannot be negative....Exited")
#---------------------------
print("-------------------------------------")
hour=0
minute=0
#converting number of seconds into hours
if(second>=3600):
    hour=second//3600
    second=second%3600
#---------------------------
#converting into minutes
if(second>=60):
    minute=second//60
    second=second%60
#---------------------------  
print("--------------------------------")  
print("equivalent time is: ", hour, "hour(s)", minute, "minute(s)", second, "second(s)")