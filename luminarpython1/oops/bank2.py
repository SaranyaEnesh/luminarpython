import datetime
class person:
    def setValues(self,pname,age):
        self.pname=pname
        self.age=age
    def printValues(self):
        print(self.pname)
        print(self.age)
class Bank(person):
    bname="SBI"
    def __init__(self,acno):
        self.acno=acno
        self.balance=3000

    def deposit(self,amount):
        self.balance+=amount
        print("your",Bank.bname,"has been cerdited with",amount,"on",datetime.data.today)
    def withdraw(self,amount):
        if(amount>self.balance):
            print("transation has been canceled")
        else:
            self.balance-=amount
            print("your",self.bname,"has been debited with",amount,"on",datetime.date.today)
    def balanceEnquiry(self):
        print("current balance",self.balance)
obj=Bank(100)
obj.setValues("saranya",21)
obj.printValues()

