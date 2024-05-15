from custome_exception import CustomError

num = int(input('Enter number:'))

try:
	if num % 2 == 0:
		print('Even number')
	else:
		raise CustomError

except NameError as e:
	print(e)

except IndexError as e:
	print(e)

except CustomError as e:
	print(e)

except Exception as e:
	print(e)