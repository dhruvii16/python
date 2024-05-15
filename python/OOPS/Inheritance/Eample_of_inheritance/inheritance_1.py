#example of child class

class Emp(Person):
    def print(self):
        print('Emp class called')

emp_details = Emp('Dhruvi', 21)
emp_details.Display()
emp_details.print()