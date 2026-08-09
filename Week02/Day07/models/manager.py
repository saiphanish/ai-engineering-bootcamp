class Manager():

    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display(self):
        print(f"Name : {self.name}")
        print(f"Department : {self.department}")