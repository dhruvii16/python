first = float(input("Enter First Number:"))
second = float(input("Enter Second Number:"))


print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')
print('5.Modulus')

operator = input("Enter Operation:")

if operator == '1':
	print("Addition:",first + second)
elif operator == '2':
	print("Subtraction:",first - second)
elif operator == '3':
	print("Multiplication:",first * second)
elif operator == '4':
	print("Division:",first / second)
elif operator == '5':
	print("Modulus:",first % second)
else:
	print("Invalid operator")