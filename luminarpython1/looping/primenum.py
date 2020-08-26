#program to check primenum or not

num=int(input("enter a number"))#9
flag=0
for i in range(2,num):#2.....8
    if(num%i==0):#9%3==0 flag=1
        flag=1
        break
    else:
        flag=0
if(flag>0):
    print("not prime")
else:
    print("prime")
