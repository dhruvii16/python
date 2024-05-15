def fah(fahrenheit):
	ans = (fahrenheit - 32) * 5/9
	return ans

fahrenheit = float(input('Enter temperature in fahrenheit:'))
print('celsius to fahrenhiet:',fah(fahrenheit))