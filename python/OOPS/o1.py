class Employee:
	emp_code=0
	emp_name=''

obj=Employee()

X=int(input('Enter the Emp code : '))
Y=(input('Enter The name of employee :'))

obj.emp_code=X
obj.emp_name=Y

print("Employee Code",obj.emp_code)
print("Employee Name",obj.emp_name)