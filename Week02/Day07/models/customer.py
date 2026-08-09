class customer:

    def __init__(self,name,city,phone):

        self.name=name
        self.city=city
        self.phone=phone

    def display(self):
    
            print(f"Name : {self.name}")
            print(f"City : {self.city}")
            print(f"Phone : {self.phone}")