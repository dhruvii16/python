a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))

if (a > b) and (a > c):
	print("a is big")

elif (b > a) and (b > c):
	print("b is big")

else:
	print("c is big")