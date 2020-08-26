class Parent:
    def property(self):
        print("50kg gold 10 lack ")
    def marriage(self):
        print("with gopal")
class Child(Parent):
    def marriage(self):
        print("with dq")
c=Child
c.property()
c.marriage()