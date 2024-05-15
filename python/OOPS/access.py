class Employee:
	__emp_code=0 # double underscore that means the private 
	__emp_name='' 

	def setval(self,code,name):
		self.__emp_code=int(input('Enter the Emp code : '))
		self.__emp_name=(input('Enter The name of employee :'))
	def getval(self):
		X=self.__emp_code
		Y=self.__emp_name

obj=Employee()
obj.getval(obj.X,obj.Y)
print("Employee code : ",)
print("Employee Name : ",)


# this program is Continued By Dhruvi Patel Because The HR wann to be sleep 