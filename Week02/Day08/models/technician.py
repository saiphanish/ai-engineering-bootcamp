from models.employee import Employee

class Technician(Employee):

    def __init__(self, name, phone, experience, skills):

        super().__init__(name, phone)

        self.experience = experience
        self.skills = skills

    def display(self):

        super().display()

        print("Experience:", self.experience)

        print("Skills:", self.skills)
