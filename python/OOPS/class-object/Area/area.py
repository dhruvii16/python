from com import Area

print('option to find area')
print('For circal = 	1')
print('For triangle = 	2')
print('For ractangal = 3')
print('For square = 	4')

option = int(input('select option :'))

obj = Area()

if option == 1:
	r=int(input('enter the radius'))
	obj.circal(r)

elif option == 2:
	b=int(input('enter the base'))
	h=int(input('enter the hight'))
	obj.triangle(b,h)

elif option == 3:
	l=int(input('enter the length'))
	w=int(input('enter the width'))
	obj.ractangal(l,w)

elif option == 4:
	a=int(input('enter the radius'))
	obj.square(a)
	
else:
	print("invalid input")