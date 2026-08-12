from models.technician import Technician
from models.manager import Manager

employees = [

    Technician(

        "Phanish",

        "9999999999",

        12,

        ["Bed Bugs", "Cockroaches"]

    ),

    Manager(

        "Sai",

        "8888888888",

        "Operations"

    )
]

for employee in employees:

    print("=" * 40)

    employee.display()