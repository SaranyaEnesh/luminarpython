class parent:
    def m1(self):
        print("inside parent")
class child():
    def m2(self):
        print("inside child")
class subchild(child,parent):
    def m3(self):
        print("inside subchild")

p=parent()
p.m1()
c=child()
c.m2()
s=subchild()
s.m3()
s.m2()
s.m1()
