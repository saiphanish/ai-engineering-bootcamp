service_cost = float(input("Enter service cost: "))

if service_cost > 1000:
    discount = 15
elif service_cost > 500:
    discount = 10
else:
    discount = 0

discount_cost = service_cost * discount / 100
discounted_price = service_cost - discount_cost

gst = 0.18 * discounted_price
final_cost = discounted_price + gst

print("=" * 30)
print("Discount Calculator")
print("=" * 30)
print(f"Original Cost: {service_cost:.2f}")
print(f"Discount: {discount:.2f}%")
print(f"GST: {gst:.2f}")
print(f"Final Amount: {final_cost:.2f}")
