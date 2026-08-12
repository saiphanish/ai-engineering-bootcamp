from models.employee import Employee

class Manager(Employee):

    def work(self):

        print(f"{self.name} is assigning technicians.")