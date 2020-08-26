class employee:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def printVal(self):
        print(self.id)
        print(self.name)
        print(self.sal)
    def __str__(self):
        return self.name
obj=employee(101,"ajay",25000)
obj2=employee(102,"sajay",25000)
obj3=employee(103,"vijay",25000)
ls=[]
ls.append(obj)
ls.append(obj2)
ls.append(obj3)
for emp in ls:
    if(emp.sal>32000):
        print(emp)
