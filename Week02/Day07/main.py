from models.customer import customer
from models.technician import Technician
from models.serviceorder import ServiceOrder
from models.manager import Manager


customer = customer(
    "Sai",
    "Hyderabad",
    "9999999999"
)

technician = Technician(
    "Phanish",
    12,
    ["Bed Bugs","Cockroaches","Termites"]
)

manager = Manager(
    "Sai",
    "IT"
)
order = ServiceOrder(
    customer,
    technician,
    manager,
    "Bed Bugs",
    2500
)

order.display()