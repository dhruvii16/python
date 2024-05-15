from abc import ABC,abstractmethod
class car(ABC):
    def milege(self):
        pass

class Tesla(car):
    def milege(self):
        print('Milege is 30kmph')

class Suzuki(car):
    def milege(self):
        print('milege is 25kmph')

class Renault(car):
    def milege(self):
        print('milege is 27kmph')

class Duster(car):
    def milege(self):
        print('milege is 24kmph')

t = Tesla()
t.milege()

s = Suzuki()
s.milege()

r = Renault()
r.milege()

d = Duster()
d.milege()