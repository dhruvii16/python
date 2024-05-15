def max(a,b,c):
	if (a > b) and (a > c):
		largest = a
	elif (b > a) and (b > c):
		largest = b
	else:
		largest = c
	return largest

a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))
print('Maximum Number is:',max(a,b,c))