from models.employee import Employee

class Manager(Employee):

    def __init__(self, name, phone, department):

        super().__init__(name, phone)

        self.department = department

    def display(self):

        super().display()

        print("Department:", self.department)