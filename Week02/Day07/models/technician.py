class Technician:

    def __init__(self, name, experience, skills):

        self.name = name
        self.experience = experience
        self.skills = skills

    def display(self):

        print(f"Technician : {self.name}")
        print(f"Experience : {self.experience} Years")

        for skill in self.skills:
            print(f" - {skill}")