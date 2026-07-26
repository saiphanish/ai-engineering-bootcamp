customer_name = input("Enter customer name: ")
technician_name = input("Enter technician name: ")
service_type = input("Enter service type: ")
service_cost = float(input("Enter service cost: "))

gst = 0.18 * service_cost
total_cost = service_cost + gst

print("=" * 30)
print("Service Calculator")
print("=" * 30)
print(f"Customer Name: {customer_name}")
print(f"Technician Name: {technician_name}")
print(f"Service Type: {service_type}")
print(f"Service Cost: {service_cost:.2f}")
print(f"GST: {gst:.2f}")
print(f"Total Cost: {total_cost}")
