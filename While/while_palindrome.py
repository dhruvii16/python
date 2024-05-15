num = int(input('Enter number:'))
box = 0
temp = num

while num > 0:
	rem = num % 10
	box = box * 10 + rem
	num = int(num / 10)

if box == temp:
	print('number is palindrome')    #121,242
else:
	print('Number is not palindrome ')