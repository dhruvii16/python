#build-in exception
#custom exception

#try:
#	print(x)
#except:
#	print('Name Error')

#mylist = [10,20,30,40]
#try:
#	print(mylist[1])
#except:
#	print('Error')

from math import factorial

num = int(input('Enter NUmber:'))

try:
	ans = factorial(num)
	print(ans)
except:
	print('Error')