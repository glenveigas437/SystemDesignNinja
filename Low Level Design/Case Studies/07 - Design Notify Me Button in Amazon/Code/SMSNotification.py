from ObserverInterface import ObserverInterface

class SMSNotification(ObserverInterface):
    def __init__(self, phoneNumber, observableObject):
        self.phoneNumber = phoneNumber
        self.observableObject = observableObject
    
    def update(self):
        message = f"The Stock of {self.observableObject.productName} has been Updated to {self.observableObject.getStockCount()}"

        self.sendEmail(self.phoneNumber, message)
    
    def sendEmail(self, phoneNumber, message):
        print(f"Sending SMS to {phoneNumber} that {message}")