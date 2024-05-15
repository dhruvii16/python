def sum_of_digit(num):
	digit_sum = 0 

	while num > 0:
		rem = num % 10
		digit_sum = digit_sum + rem
		num = int(num/10)
	return digit_sum

num = int(input('Enter Number:'))
print('Sum of digit is:',sum_of_digit(num))
		