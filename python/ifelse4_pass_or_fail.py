Python = int(input("Enter marks of Python:"))
Java = int(input("Enter marks of Java:"))
C = int(input("Enter marks of C:"))
Php = int(input("Enter marks of Php:"))
Android = int(input("Enter marks of Android:"))

Total = Python + Java + C + Php + Android
Per = Total / 5

print("Total:",Total)
print("Percentage:",Per)

if Per >= 35:
	print("Pass")
else:
	print("Fail")