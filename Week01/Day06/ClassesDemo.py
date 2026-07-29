class Customer:
    def __init__(self, name, service, city):
        self.name = name
        self.service = service
        self.city = city

    def welcome(self):
        print(f"Welcome {self.name}")

customer = Customer("Sai", "Bed Bugs", "Hyderabad")
# print(f"Customer Name: {customer.name}")
# print(f"Service: {customer.service}")
# print(f"City: {customer.city}")

customer.welcome()

class ServiceOrder:
    def __init__(self, customer_name, service_type, service_cost):
        self.customer_name = customer_name
        self.service_type = service_type
        self.service_cost = service_cost

    def calculate_gst(self):
        gst = 0.18 * self.service_cost
        return gst

order = ServiceOrder("Sai", "Bed Bugs", 1000)
print(f"Customer Name: {order.customer_name}")
print(f"Service Type:{order.service_type}")
print(f"Service Cost: {order.service_cost}")
print(f"GST: {order.calculate_gst()}")
