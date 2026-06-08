str=input("enter a string")
a_count=0
e_count=0
i_count=0
o_count=0
u_count=0
for ch in str:
    if ch=='A' or ch=='a':
        a_count+=1
    elif ch=='E' or ch=='e':
        e_ += 1
    elif ch=='I' or ch=='i':
        i_count += 1
    elif ch=='O' or ch=='o':
        o_count += 1
    elif ch=='U' or ch=='u':
        u_count += 1

if a_count > 0:
    print("a :", a_count)
if e_count > 0:
    print("e :", e_count)
if i_count > 0:
    print("i :", i_count)
if o_count > 0:
    print("o :", o_count)
if u_count > 0:
    print("u :", u_count)