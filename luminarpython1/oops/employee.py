class Employee:
    def setEmployee(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary
    def printValues(self):
        print(self.eid)
        print(self.ename)
        print(self.desig)
        print(self.salary)
obj=Employee()
obj.setEmployee(100,"saranya","ceo",25000)
obj.printValues()

