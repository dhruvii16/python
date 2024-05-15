mylist = [6,4,8,0,2]
for i in range(0,5):
	for j in range(i+1,5):
		if mylist [i] < mylist[j]:
			c = mylist[i]
			mylist[i] = mylist[j]
			mylist[j] = c
print(mylist)