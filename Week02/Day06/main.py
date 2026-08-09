from models.customer import Customer
from services.file_service import load_customers
from services.file_service import save_customer

while True:

    print("\n" + "=" * 40)
    print("      PestPac Management System")
    print("=" * 40)

    print("1. Add Customer")
    print("2. View Customers")
    print("3. Search Customer")
    print("4. Exit")

    choice = input("Enter Choice : ")

    print(f"You entered: '{choice}'")
    if choice == "1":
        print(f"You entered: '{choice}'")
        name = input("Customer Name : ")
        city = input("City : ")
        phone = input("Phone : ")

        customer = Customer(name, city, phone)

        save_customer(customer)

        print("Customer Saved Successfully")

    elif choice == "2":
        print(f"You entered: '{choice}'")
        customers = load_customers()

        print("=" * 40)

        for customer in customers:

            # print(customer)
            print(f"""
            Customer : {customer['name']}
            City     : {customer['city']}
            Phone    : {customer['phone']}
            """)

        print("=" * 40)

    elif choice == "3":
        print(f"You entered: '{choice}'")
        customers = load_customers()      # <-- ADD THIS

        search_name = input("Enter customer name : ")
        found = False

        for customer in customers:

            if customer["name"].lower() == search_name.lower():

                print(f"""
    Customer : {customer['name']}
    City     : {customer['city']}
    Phone    : {customer['phone']}
    """)

                found = True

        if not found:
            print("Customer not found.")