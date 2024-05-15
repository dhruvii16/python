#base class
class Grandfather:
    def __init__(self,grandfathername):
        self.grandfathername = grandfathername

#intermediate class
class Father(Grandfather):
    def __init__(self,fathername,grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self,grandfathername)

#child class
class Son(Father):
    def __init__(self,sonname,fathername,grandfathername):
        self.sonname = sonname
        Father.__init__(self,fathername,grandfathername)

    def print_name(self):
        print('Grand-FatherName:',self.grandfathername)
        print('Father Name:',self.fathername)
        print('Son Name:',self.sonname)

s1 = Son('Dhruvu', 'Papppa', 'Dada')  
print (s1.grandfathername)  
s1.print_name()  

# #base class
# class Animal:
#     def speak(self):
#         print("Animal is Speaking")

# #Intermediate class
# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# #child class
# class DogChild(Dog):
#     def eat(self):
#         print("Dog is Eating")

# d = DogChild()
# d.speak()
# d.bark()
# d.eat()