class P1:
    def m1(self):
        print("m1 method")
class P2:
    def m1(self):
        print("m2 method")
class child(P1,P2):
    pass



obj=child()
obj.m1()






