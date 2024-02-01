first = int(input("Enter First Number:"))
operator = input("Enter Operator(+,-,*,/,%):")
second = int(input("Enter Second Number:"))

if operator == '+':
	print("Addition:",first + second)
elif operator == '-':
	print("Subtraction:",first - second)
elif operator == '*':
	print("Multiplication:",first * second)
elif operator == '/':
	print("Division:",first / second)
elif operator == '%':
	print("Modulus:",first % second)
else:
	print("Invalid operator")