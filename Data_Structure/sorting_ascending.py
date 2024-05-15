mylist = [4,2,6,9,0]
for i in range(0,5):
	for j in range(i+1,5):
		if(mylist[j] < mylist[i]):
			c = mylist[i]
			mylist[i] = mylist[j]
			mylist[j] = c
print(mylist)