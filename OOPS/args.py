# *args tuple

#def add(*args):
#	print(args)

#add(10,20,30)
#add(10,20,30,50)

def add(*args):
	sum = 0
	for i in args:
		sum = sum + i
	print('sum:',sum)

add(10,20)
add(10,4,5)