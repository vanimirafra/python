class P:
    def m1(self):
        print("parent method")
class C1(P):
    def m2(self):
        print("child1 method")
class C2(P):
    def m3(self):
        print("child2 method")




obj=C1()
obj.m2()
obj.m1()
obj=C2()
obj.m3()
obj.m1()
