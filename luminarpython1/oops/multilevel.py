class parent:
    def m1(self):
        print("inside parent")
class child(parent):
    def m2(self):
        print("inside child")
class subchild(child):
    def m3(self):
        print("inside subchild")

su=subchild()
su.m1()
su.m2()
su.m3()

ch=child()
ch.m2()
ch.m1()

p=parent()
p.m1()