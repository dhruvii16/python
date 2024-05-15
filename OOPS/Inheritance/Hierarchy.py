#parent class
class Parent:
    def func(self):
        print("Parent Class")

class Child1(Parent):
    def func1(self):
        print("Child class")

class Child2(Parent):
    def Func2(self):
        print("Second Child class")

object1 = Child1()
object2 = Child2()
object1.func()
object1.func1()
object2.func()
object2.Func2()