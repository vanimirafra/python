class X():
    def m1(self):
        print("I am a X")
    #pass    
    
class Y():
    def m1(self):
        print("I am a Y")
    
class A(X, Y):
    def m1(self):
        print("I am a A")
     #pass 
class B(Y, X):
     def m1(self):
         print("I am a B")


class F(A, B):
    #def m1(self):
        #print("I am a F")


obj=F()
obj.m1()

#F.__mro__
#F.mro()
