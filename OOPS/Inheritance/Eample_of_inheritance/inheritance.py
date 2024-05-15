#example of parent class 
class Person(object):

#constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def Disply(self):
        print(self.name, self.id)

emp = Person('Dhruvi', 21)
emp.Disply()