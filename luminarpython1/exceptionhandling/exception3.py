num1=int(input("enter value for num1"))
num2=int(input("enter value for num2"))
try:
    res=num1/num2
    print("reslut=",res)
except Exception as e:
    print(e.args)
finally:
    print("we have database transaction")
    print("file operation")
    print("process completed ")