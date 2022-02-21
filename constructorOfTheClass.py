# Defining constructor for the class

class Employee:

    def __init__(self, i):
        self.employee_id = i

    def work(self):
        print(f'{self.employee_id} is working')

emp = Employee(100)
emp.work()
