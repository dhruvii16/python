import math

side = float(input("Enter length of side:"))

area = 0.25 * math.sqrt(5*(5 + 2 * math.sqrt(5))) * side**2

print(f"Area of pentagon is: {area:.2f}")