class XYZ():
    def websites(self):
        print('java')

    def topic(self):
        print('python')
    
    def type(self):
        print('c')

class PQR():
    def websites(self):
        print('Sql')
    
    def topic(self):
        print('Mysql')
    
    def type(self):
        print('oracle')

obj_1 = XYZ()
obj_2 = PQR()

for domain in (obj_1,obj_2):
    domain.websites()
    domain.topic()
    domain.type()