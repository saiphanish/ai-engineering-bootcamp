def calculate_gst(service_cost: float) -> float:
    gst = service_cost * 0.18
    return gst

try:   
    customer = input("Enter Customer Name:")
    print(f"Customer: {customer}")
    service_type = input("Enter Service Type:")
    print(f"Service Type: {service_type}")
    service_cost = float(input("Enter Service Cost:"))
    if service_cost < 0:
        raise ValueError("Cost cannot be negative")
    gst_amount = calculate_gst(service_cost)
    print(f"GST Amount: {gst_amount:.2f}")
    print(f"Total Cost: {service_cost + gst_amount:.2f}")
except ValueError as ex:
    print(ex)
finally:
    print("Thank you for using SPac.")

