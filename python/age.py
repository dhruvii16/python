age = int(input("Enter age:"))

if age >= 18:
	voterid = input("Do you have voterid:")
	if voterid == 'yes':
		print("You can give vote.")
	else:
		print("You can't.")
else:
	print("You are not eligible for vote")