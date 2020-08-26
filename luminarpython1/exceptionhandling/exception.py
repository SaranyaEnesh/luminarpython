num1=int(input("enter value for num1"))
num2=int(input("enter value for num2"))
try:
    res=num1/num2
    print("reslut=",res)
    print("we have database transaction")
    print("process completed ")
except:
    print("exception occoured")