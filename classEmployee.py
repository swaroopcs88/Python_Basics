# class Employee
class Employee:
    emp_id = 12

    def work(self):
        print(f'{self.emp_id} is working')
        


emp = Employee()
print(type(emp))
emp.work()
