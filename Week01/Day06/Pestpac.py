class Customer:
    def __init__(self, name, city, phone):
        self.name = name
        self.city = city
        self.phone = phone

    def display(self):
        print(f"Customer: {self.name}")
        print(f"City: {self.city}")
        print(f"Phone: {self.phone}")

customer = Customer("Sai", "Hyderabad", "9999999999")
customer.display()

class ServiceOrder:
    def __init__(self, customer, service, cost):
        self.customer = customer
        self.service = service
        self.cost = cost

    def calculate_discount(self):
        discount = self.cost * .10
        print(f"Discounted Price is: {discount}")

    def calculate_gst(self):
        gst = self.cost * .18
        print(f"Gst is: {gst}%")

    def calculate_total(self):
        discountedprice = self.cost - self.cost * .10
        gst = discountedprice * .18
        total = discountedprice + gst
        print(f"Total is: {total}")

    def display_invoice(self):
        print("=" * 40)
        print("SPac Invoice")
        print("=" * 40)
        print(f"Customer: {self.customer}")
        print(f"Service: {self.service}")
        print(f"Cost: {self.cost}")
        self.calculate_discount()
        self.calculate_gst()
        self.calculate_total()
        print("=" * 40)

serviceorder = ServiceOrder("Sai", "BedBugs", 1000)
serviceorder.display_invoice()