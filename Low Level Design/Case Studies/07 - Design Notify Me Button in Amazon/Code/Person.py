from EmailNotification import EmailNotification
from SMSNotification import SMSNotification

class Person:
    def __init__(self, personName, email, phoneNumber):
        self.personName = personName
        self.email = email
        self.phoneNumber = phoneNumber
        self.wishList = []
    
    def setEmailNotification(self, productObject):
        self.emailNotificationObject = EmailNotification(self.email, productObject)
        self.addToWishList(productObject)
        return self.emailNotificationObject
    
    def setSMSNotification(self, productObject):
        self.setSMSNotificationObject = SMSNotification(self.phoneNumber, productObject)
        self.addToWishList(productObject)
        return self.setSMSNotificationObject
    
    def addToWishList(self, productObject):
        self.wishList.append(productObject)
    
    def viewProducts(self):
        for product in self.wishList:
            print(f"Stock of {product.productName} is {product.stockCount}")
