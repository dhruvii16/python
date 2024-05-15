num = int(input('Enter number:'))
sqr = 0

while num > 0:
	rem = num % 10
	sqr = sqr + rem * rem
	num = int(num/10)
print(sqr)