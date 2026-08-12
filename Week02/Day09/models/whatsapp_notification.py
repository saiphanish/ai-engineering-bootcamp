from models.notification import NotificationService

class WhatsAppNotification(NotificationService):
    
    def send(self, message):

        print("WhatsApp:", message)