from models.employee import Employee

class Technician(Employee):

    def __init__(self, name, experience, skills):

        super().__init__(name, experience)
        self.skills = skills

    def display(self):

        print(f"Technician : {self.name}")
        print(f"Experience : {self.experience} Years")

        for skill in self.skills:
            print(f" - {skill}")