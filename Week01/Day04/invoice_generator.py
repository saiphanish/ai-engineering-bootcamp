def calculate_discount(cost):
    if cost >= 500:
        discount = 10
    else:
        discount = 0
    return discount

def calculate_gst(cost):
    gst = 0.18 * cost
    return gst

def calculate_final_cost(cost):
    discount = calculate_discount(cost)
    gst = calculate_gst(cost)
    discounted_price = cost - (cost * discount /100)
    final_cost = discounted_price + gst
    return discounted_price, final_cost
 

customer_name = input("Enter customer name: ")
technician_name = input("Enter technician name: ")
service_type = input("Enter service type: ")
service_cost = float(input("Enter service cost: "))
discounted_price, final_cost = calculate_final_cost(service_cost)

print("=" * 30)
print("Invoice Generator")
print("=" * 30)
print(f"Customer Name: {customer_name}")
print(f"Technician Name: {technician_name}")
print(f"Service: {service_type}")
print(f"Original Cost: {service_cost:.2f}")
print(f"Discount: {calculate_discount(service_cost)}%")
print(f"GST: {calculate_gst(service_cost):.2f}")
print(f"Discounted Price: {discounted_price:.2f}")
print(f"Final Cost: {final_cost:.2f}")
