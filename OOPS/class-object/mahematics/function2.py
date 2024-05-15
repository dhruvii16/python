from common import Math

#sum_digit,rev,armstrong,mul_digit
num = int(input('enter the value of num'))
print('option to find calculate')
print('For Addition = 	1')
print('For Multipication = 2')
print('For armstrong = 3')
print('For reverce = 4')
print('For palindrom = 5')
print('Addition of Enterd Degit = 6')
print('Multipication of Enterd Degit = 7')

m=Math()

option = int(input('select option :'))


if option == 1:
	m.sum_digit(num)

elif option == 2:
	m.mul_digit(num)

elif option == 3:
	m.armstrong(num)

elif option == 4:
	m.rev(num)

elif option == 5:
	m.pal(num)

elif option == 6:
	m.Adddegit(num)

elif option == 7:
	m.Muldegit(num)
else:
	print("invalid input")