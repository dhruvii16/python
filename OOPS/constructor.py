#class abc:
#	def __init__(self):
#		print('constructor')
#	def __str__(self):

class abc:
	def hello(self):
		print('hello')

	def __str__(self):   #method that convert class object into string
	   return 'hello'

obj = abc()
obj.hello()
print(obj)