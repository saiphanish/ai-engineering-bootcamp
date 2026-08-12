from models.notification import NotificationService

class EmailNotification(NotificationService):

    def send(self, message):
        
        print("Email:", message)