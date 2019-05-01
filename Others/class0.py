
class Employee:

    num_of_emps = 0
    raise_amout = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amout)


print(Employee.num_of_emps)
emp_1 = Employee('Xuelei', 'Pan', 25000)
print(Employee.num_of_emps)
emp_2 = Employee('Test', 'User', 5000)
print(Employee.num_of_emps)

print(Employee.raise_amout)
print(emp_1.raise_amout)
emp_2.raise_amout = 1.05
print(emp_2.raise_amout)

# print(emp_1.fullname())
# print(emp_1.pay)
# print(emp_2.pay)
# print(Employee.fullname(emp_2))
