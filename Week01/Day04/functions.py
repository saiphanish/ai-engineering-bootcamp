def welcome(customer_name):
    print(f"welcome {customer_name}")

def technician(technician_name):
    print(f"Technician: {technician_name}")

def service(customer, service_type):
    print(f"{customer} booked {service_type}")

def add(a, b):
    return a + b

def calculate_gst(cost):
    gst = 0.18 * cost
    return gst

def calculate_bill(cost):
    gst = 0.18 * cost
    total_cost = cost + gst
    return total_cost, gst

def apply_discount(cost, discount = 10):
    discount_cost = cost * discount / 100
    discounted_price = cost - discount_cost
    return discounted_price

welcome("Sai")
welcome("John")
welcome("David")    

technician("Phanish")
technician("Robert")

service("Sai", "Bed Bugs")

result = add(10, 20)
print(f"Result: {result}")

gst = calculate_gst(100)
print(f"GST: {gst}")

total_bill, gst = calculate_bill(1000)
print(f"Total Bill: {total_bill:.2f}")
print(f"GST: {gst:.2f}")

print(f"Discounted Price: {apply_discount(1000):.2f}")
apply_discount(cost = 1000, discount =15)
print(f"Discounted Price with keyword arguments: {apply_discount(cost = 1000, discount =15):.2f}")