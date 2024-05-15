# class Calculation1:
#     def Sum(self,a,b):
#         return a+b;

# class Calculation2:
#     def Sub(self,a,b):
#         return a-b;

# class Derived(Calculation1,Calculation2):
#     def Divide(self,a,b):
#         return a/b;

# d = Derived()
# print(d.Sum(10,20))
# print(d.Sub(10,20))
# print(d.Divide(10,20))

#Base Class 1
class Mother1:  
    mothername1 = ""  
    def mother1(self):  
        print(self.mothername1)  
  
#Base class 2  
class Father1:  
    fathername1 = ""  
    def father1(self):  
        print(self.fathername1)  
  
#Derived class  
class Son1(Mother1, Father1):  
    def parents1(self):  
        print ("Father name is :", self.fathername1)  
        print ("Mother name is :", self.mothername1)  
  
s1 = Son1()  
s1.fathername1 = "Papppa"  
s1.mothername1 = "Dhruvu"  
s1.parents1()  