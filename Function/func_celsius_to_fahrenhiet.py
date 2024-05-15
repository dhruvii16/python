def cel(celsius):
	ans = (celsius * 9/5) + 32
	return ans

celsius = float(input('Enter temperature in celsius:'))
print('celsius to fahrenhiet:',cel(celsius))