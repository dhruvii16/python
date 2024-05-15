from math import factorial

num = int(input('Enter Number:'))

try:
	ans = factorial(num)
	print(ans)

except NameError as e:
	print(e)

except IndexError as e:
	print(e)

except ValueError as e:
	print(e)

except Exception as e:
	print(e)
