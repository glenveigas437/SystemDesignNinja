from ObserverInterface import ObserverInterface

class EmailNotification(ObserverInterface):
    def __init__(self, email, observableObject):
        self.email = email
        self.observableObject = observableObject
    
    def update(self):
        message = f"The Stock of of {self.observableObject.productName} has been Updated to {self.observableObject.getStockCount()}"

        self.sendEmail(self.email, message)
    
    def sendEmail(self, email, message):
        print(f"Sending Email to {email} that {message}")