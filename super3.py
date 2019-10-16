#define one supeclass and 2 subclasses create objects for each sub-class and call functions present in subclass and class



#superclass 
class Project:
      def __init__(self,no,name):
          self.no=no
          self.name=name
      def details(self):
          #return "no=%d name=%s" %(self.no,self.name)
           print("no=%d name=%s"%(self.no,self.name))



#subclass-1
class Development(Project):
      def __init__(self,no,name,lan):
          super().__init__(no,name)
          #Project.__init__(self,no,name)             #inheriting the property of  superclass
          self.lan=lan
      def details(self): #print the details
           print("lan=%s no=%d name=%s"%(self.lan,self.no,self.name))





#subclass-2
class Testing(Project):
      def __init__(self,no,name,pas):

          super().__init__(no,name)
          #Project.__init__(self,no,name)           #inheriting the property of superclass
          self.pas=pas
      def details(self):
          print("pas=%s no=%d name=%s" %(self.pas,self.no,self.name))


obj1=Development(5,"lhm","python")                #create object for subclass-1
obj2=Testing(5,"lhm","pas")                       #create object for subclass-2
obj1.details()
obj2.details()
          
