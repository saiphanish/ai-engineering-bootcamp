class Customer:
    
    def __init__(self, name, city, phone):

        self.name = name
        self.city = city
        self.phone = phone

    def to_dict(self):

        return{
            "name": self.name,
            "city": self.city,
            "phone": self.phone
        }