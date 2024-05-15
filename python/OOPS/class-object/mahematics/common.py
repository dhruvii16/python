class Math:
	def sum_digit(self,num):
		x = range(1,num+1)
		sum=0
		for i in x:
			sum = sum + i
		print(sum)

	def mul_digit(self,num):
		x=range(1,num+1)
		mul=1
		for i in x:
			mul=mul*i
		print("multiplicatin of 1 to 5 is=",mul)

	def armstrong(self,num):
		box=0
		temp=num
		while num>0:
			rem=num%10
			box=box+rem*rem*rem
			num=int(num/10)

		if box==temp:
			print("Number is Armstroms!")
		else:
			print("Number is not Armstroms")
		
	def rev(self,num):
		box=0;

		while num>0:
	 		rem=num%10
	 		box=box*10+rem
	 		num=int(num/10)
		print(box)

	def pal(self,num):
		box=0
		temp=num

		while num>0:
			rem=num%10
			box=box*10+rem
			num=int(num/10)

		if box==temp:
			print("Number is Palindrom!")
		else:
			print("Number is not Palindrom")

	def Adddegit(self,num):
		#num=int(input("Enter Number:"))
		box=0

		while num>0:
			rem=num%10
			box=box+rem
			num=int(num/10)

		print(box)

	def Muldegit(self,num):
		#num=int(input("Enter Number:"))
		box=1

		while num>0:
			rem=num%10
			box=box*rem
			num=int(num/10)

		print(box)
