mylist = [2,5,3,8,6,1,9]
box = 0
for i in mylist:
	if i % 3 == 0:
		box = box + 1
		if box == 0:
			print('Not Available')
		else:
			print('Total=',box)