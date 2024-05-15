class Base1:  
    def __init__(self):  
          self.p = "Python"  
          self.__q = "Java"  
  
# Creating a derived class  
class Derived1(Base1):  
      def __init__(self):  
  
# Calling constructor of  
# Base class  
        Base1.__init__(self)  
        print("We will call the private member of base class: ")  
        print(self.__q)  
  
  
# Driver code  
obj_1 = Base1()  
print(obj_1.p)  