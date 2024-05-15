def calculator(a,op,b):
	if op == '1':
		result  = a+b
	elif op == '2':
		result = a-b
	elif op == '3':
		result = a*b
	elif op == '4':
		result = a/b
	elif op == '5':
		result = a%b
	return result

a = float(input('Enter First Number:'))
b = float(input('Enter Second Number:'))

print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')
print('5.Modulus')

op = input("Enter Operation:")

print('Result:',calculator(a,op,b))



