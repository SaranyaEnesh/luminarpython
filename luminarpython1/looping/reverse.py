num=int(input("enter a number"))#123
res=0
while(num!=0):
    digit=num%10#123%10=3
    res=(res*10)+digit#0*10+3=3
    num=num//10#123//10=12
print(res)