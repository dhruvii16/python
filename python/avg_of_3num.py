a = int(input("Enter number of a:"))
b = int(input("Enter number of b:"))
c = int(input("Enter number of c:"))

if a > b:
	if a > c:
		print("A is greater than b and c")
	else:
		print("C is grater than a and b")
else:
	if b > c:
		print("B is greater than a and c")
	else:
		print("C is greater than a and b")

