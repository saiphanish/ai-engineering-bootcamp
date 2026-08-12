class Employee:

    def __init__(self, name, phone):

        self.name = name
        self.phone = phone

    def display(self):

        print("Name :", self.name)
        print("Phone:", self.phone)