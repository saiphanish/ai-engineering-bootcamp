from models.service_type import ServiceType
from models.customer import Customer

service = ServiceType.BED_BUGS

customer = Customer("Sai", "Hyd", "123456789")

print(service)
print(service.value)
print(customer)