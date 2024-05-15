#program for protected members

class Base:
    def __init__(self):
        self._p = 80

class Derived:
    def __init__(self):

        #call constructor of base class
        Base.__init__(self)
        print('Call the protected member of class:',self._p)

        #modifying protected variable
        self._p = 400
        print('call protected member outside the class',self._p)

obj = Derived()
obj1 = Base()
print('Access the protected member of obj:',obj._p)
print('Access the protected member of obj1:',obj1._p)