from models.employee import Employee

class Technician(Employee):

    def work(self):

        print(f"{self.name} is treating Bed Bugs.")