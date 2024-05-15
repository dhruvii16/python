# animal class(parent class)
# class Animal:
#     def speak(self):
#         print("Animal is speaking")

# dog class(child class)
# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# d = Dog()
# d.speak()
# d.bark()

#parent class(base class)
class Parent:
    def func(self):
        print("Parent class")

#child class(Derived class)
class Child(Parent):
    def func_1(self):
        print("Child class")

object = Child()
object.func()
object.func_1()