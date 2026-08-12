from models.notification import NotificationService

class SmsNotification(NotificationService):

    def send(self, message):

        print("SMS:", message)