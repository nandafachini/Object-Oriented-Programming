# Implement an Employee class.

# ----------------------------
# | Employee                 |
# ----------------------------
# | name                     |
# | salary                   |
# ----------------------------
# increase_salary(percentage)|
# ----------------------------


class Employee:
    def __init__(self):
        self.name = None
        self.salary = None

    def increase_salary(self, percentage):
        self.salary = self.salary + (self.salary * percentage/100)
        return self.salary

name = input("Enter the employee's name: ")
salary = int(input("Enter employee salary: "))
percentage = int(input("Enter the percentage to be added to the employee's salary: "))

employee1 = Employee()
employee1.name = name
employee1.salary = salary
employee1.salary = employee1.increase_salary(percentage)
print(f"The employee's new salary is $: {employee1.salary}")