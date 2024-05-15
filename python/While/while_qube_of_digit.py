num = int(input('Enter number:'))
qube = 0

while num > 0:
	rem = num % 10
	qube = qube + rem * rem * rem
	num = int(num/10)
print(qube) 