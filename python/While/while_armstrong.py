num = int(input('Enter number:'))
box = 0
temp = num

while num > 0:
	rem = num % 10
	box = box + rem * rem * rem
	num = int(num / 10)

if box == temp:
	print('Armstrong number')     #digit -> qube -> sum 153,370,371,407
else:
	print('Not an Armstrong number')
	