class Employee:
	emp_id = 1
	emp_name = 'Dhruvi'

	def hello(self):
		print('Hello')
	def test(self):
		print('test')

obj = Employee()
print(obj.emp_id)
obj.hello()
