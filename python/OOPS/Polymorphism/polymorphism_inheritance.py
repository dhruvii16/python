class Birds:
    def intro(self):
        print('Birds')

    def flight(self):
        print('Birds can fly')

class Sparrow(Birds):
    def flight(self):
        print('Sparrow')
    
class Ostrich(Birds):
    def flight(self):
        print('Ostrich')

obj_birds = Birds()
obj_spr = Sparrow()
obj_ost = Ostrich()

obj_birds.intro()
obj_birds.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
