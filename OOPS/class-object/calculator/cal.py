from c1 import cal
a = int(input('enter the value of a'))
b = int(input('enter the value of b'))

print('option to find calculate')
print('For Addition = 	1')
print('For substraction = 	2')
print('For Multipication = 3')
print('For Divison = 	4')

option = int(input('select option :'))
obj=cal()

if option == 1:
	cal.add(a,b)

elif option == 2:
	cal.sub(a,b)

elif option == 3:
	cal.mul(a,b)

elif option == 4:
	cal.div(a,b)
else:
	print("invalid choice")