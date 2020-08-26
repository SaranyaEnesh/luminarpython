import datetime
class Bank:
    def __init__(self,acno,personname):
        self.acno=acno
        self.personname=personname
        self.balance=3000
        self.bname="SBI"
    def deposit(self,amount):
        self.balance+=amount
        print("your",self.bname,"has been cerdited with",amount,"on",datetime.data.today)
    def withdraw(self,amount):
        if(amount>self.balance):
            print("transation has been canceled")
        else:
            self.balance-=amount
            print("your",self.bname,"has been debited with",amount,"on",datetime.date.today)
    def balanceEnquiry(self):
        print("current balance",self.balance)
obj=Bank(100,"saranya")
obj.deposit(5000)
obj.balanceEnquiry()

