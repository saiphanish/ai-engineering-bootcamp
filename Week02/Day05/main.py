from models.customer import Customer
from services.file_service import save_customer

print("=" * 40)
print("PestPac Service System")
print("=" * 40)

name = input("Customer Name : ")
city = input("City : ")
phone = input("Phone : ")

customer = Customer(name, city , phone)

save_customer(customer)

print("Customer Saved Successfully")