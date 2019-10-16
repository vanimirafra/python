class A(object):
    def __init__(self,a):
        self.a=a

class B(A):
    def __init__(self,b,**kw):
        self.b=b
        super(B,self).__init__(**kw)

class C(A):
    def __init__(self,c,**kw):
        self.c=c
        super(C,self).__init__(**kw)

class D(B,C):
    def __init__(self,a,b,c,d):
        super(D,self).__init__(a=a,b=b,c=c)
        self.d=d
obj=D()

