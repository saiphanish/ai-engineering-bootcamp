from models.technician import Technician
from models.manager import Manager
from models.email_notification import EmailNotification
from models.sms_notification import SmsNotification
from models.whatsapp_notification import WhatsAppNotification

employees = [

    Technician("Phanish"),

    Manager("Sai")

]

for employee in employees:

    employee.work()

    services = [

    EmailNotification(),

    SmsNotification(),

    WhatsAppNotification()

]

for service in services:

    service.send("Service Completed")