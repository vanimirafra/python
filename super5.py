#define one supeclass and 2 subclasses create objects for each sub-class and call functions present in subclass and class



#superclass 
class Person:
      def __init__(self,age,name):
          self.age=age
          self.name=name
      def details(self):
          #return "no=%d name=%s" %(self.no,self.name)
           print("age=%d name=%s"%(self.age,self.name))



#subclass-1
class Student(Person):
      def __init__(self,age,name,no):
          super().__init__(age,name)
          #Project.__init__(self,no,name)             #inheriting the property of  superclass
          self.no=no
      def details(self): #print the details
           print("no=%d age=%d name=%s"%(self.age,self.no,self.name))





#subclass-2
class Teacher(Person):
      def __init__(self,age,name,sal):

          super().__init__(age,name)
          #Project.__init__(self,no,name)           #inheriting the property of superclass
          self.sal=sal
      def details(self):
          print("sal=%d age=%d name=%s" %(self.sal,self.age,self.name))


obj1=Student(25,"lhm",29)                #create object for subclass-1
obj2=Teacher(25,"lhm",269000)                       #create object for subclass-2
obj1.details()
obj2.details()
          
