customer = {
    "name": "Sai",
    "age": 30,
    "city": "New York"
}

""" print(customer["name"])
print(customer["age"])
print(customer["city"]) """

print(customer)

customers = [
    {"name": "Alice", "cost": 1001, "service": "Bed Bugs"},
    {"name": "Bob", "cost": 30, "service": "Cockroaches"},
    {"name": "Charlie", "cost": 35, "service": "Termites"}
]

print("=" * 30)
for customer in customers:
    print(f"Customer: {customer['name']}, Service: {customer['service']}, Cost: {customer['cost']}")
    if customer['cost'] > 1000:
        print("premium customer")
    else:
        print("Standard customer")
print("=" * 30)

""" location = ( 10.023, 76.308  )

print(location[1])

cities = { "hyderabad","hyderabad","bangalore","chennai" }
print(cities) """