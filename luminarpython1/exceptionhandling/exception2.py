num1=int(input("enter value for num1"))
num2=int(input("enter value for num2"))
lst=[1,2,3,4]
try:
    res=num1/num2
    print("reslut=",res)
    pos=int(input("enter index position"))
    print(lst[pos])
    print("we have database transaction")
    print("process completed ")
except Exception as e:
    print(e.args)