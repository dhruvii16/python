def area_of_triangle(b,h):
	area = 0.5 * b * h
	return area

ans1 = float(input('Enter Base:'))
ans2 = float(input('Enter Height:'))
print('Area of Triangle:',area_of_triangle(ans1,ans2))
	