num=int(input("enter a num"))
sum=0
while(num!=0):
    digit=num%10
    sum=sum+(digit**3)
    num=num//10
print(sum)
