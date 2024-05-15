def area_of_circle(area):
	area = 3.14 * r * r
	return area

def area_of_rec(l,w):
	area = l * w
	return area

def area_of_square(a):
	area = a * a
	return area

ans = int(input('enter area:'))
print('Area of Square:',area_of_square(ans))

def area_of_triangle(b,h):
	area = 0.5 * b * h
	return area

ans1 = float(input('Enter Base:'))
ans2 = float(input('Enter Height:'))
print('Area of Triangle:',area_of_triangle(ans1,ans2))
	
def main():
	if x==1:
		r = int(input('Enter Number of r:'))
		area_of_circle(area)
	elif x==2:
		l = int(input('Enter length:'))
		w = int(input('Enter width:'))
		area_of_rec(l,w)
	elif x==3:
		a = int(input('Enter area of a:'))
		area_of_square(a)

x = input('Enter the selected Function:')
