from models.customer import customer
from models.technician import Technician
from models.manager import Manager

class ServiceOrder:

    def __init__(self,
                 customer: customer,
                 technician: Technician,
                 manager: Manager,
                 service,
                 cost):

        self.customer = customer
        self.technician = technician
        self.manager = manager
        self.service = service
        self.cost = cost

    def display(self):

        print("="*40)

        print()
        
        self.customer.display()

        print()

        self.technician.display()

        print()

        self.manager.display()

        print()

        print(f"Service : {self.service}")
        print(f"Cost : {self.cost}")

        print("="*40)
