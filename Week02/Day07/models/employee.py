class Employee:

    def __init__(self, name, experience):

        self.name = name
        self.experience = experience
      
    def display(self):

        print(f"Name : {self.name}")
        print(f"Experience : {self.experience} Years")
