import json
import os


def save_customer(customer):

    customers = []

    if os.path.exists("data/customer.json"):

        with open("data/customer.json", "r") as file:

            if os.path.getsize("data/customer.json") > 0:
                customers = json.load(file)

    customers.append(customer.to_dict())

    with open("data/customer.json", "w") as file:

        json.dump(customers, file, indent=4)