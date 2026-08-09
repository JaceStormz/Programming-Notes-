# 08/06/2026
# employeeObj.py

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def employee_info(self):
        print(f"Id: {self.id}, Name: {self.name}")

employee1 = Employee(1, "coder")
employee2 = Employee(2, "analyst")

employee1.employee_info()
employee2.employee_info()
