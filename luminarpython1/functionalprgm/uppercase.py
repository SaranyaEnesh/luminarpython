import functools
class employee:
    def __init__(self,id,name,desig,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary
    def printemp(self):
        print("name=",self.name)
        print("desig=",self.desig)
    def __str__(self):
        return self.name
f=open("details","r")
lst=[]
for data in f:
    values=data.rstrip("\n").split(",")
    id=values[0]
    name=values[1]
    desig=values[2]
    salary=values[3]
    obj=employee(id,name,desig,salary)
    lst.append(obj)
upper=list(map(lambda emp:emp.name.upper(),lst))
salarylist=list(filter(lambda emp:int(emp.salary)>25000,lst))
maxsal=list(map(lambda emp:int(emp.salary)+5000,lst))
salarys=list(map(lambda obj:obj.salary,lst))
print(salarys)
maxval=functools.reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,salarys)
highsal=list(filter(lambda emp:emp.salary==maxval,lst))
for emp in highsal:
    print(emp)
#print(upper)
#for emp in salarylist:
 #   print(emp)
#print(maxsal)
print(maxval)



