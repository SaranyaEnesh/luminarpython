num1=int(input("entr a num1"))#10
num2=int(input("entr a num2"))#20
num3=int(input("entr a num3"))#30

if(num1>num2)&(num1>num3):#10>20&10>30
    print("max",num1)
elif(num2>num1)&(num2>num3):#20>10720>30
    print("max ",num2)
elif(num3>num1)&(num3>num2):
    print("max",num3)
else:
    print("numbers are equal")