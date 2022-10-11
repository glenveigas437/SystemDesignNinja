from IPhoneObservableInterface import IphoneObservableInterface
from Product import Product
from PlayStationObservableInterface import PlayStation5ObservableInterface
from Person import Person



iPhone14ProPlusObject = IphoneObservableInterface()
iPhone14ProPlus = Product('iPhone 14 Pro Plus', iPhone14ProPlusObject)

playStation5Object = PlayStation5ObservableInterface()
playStation5 = Product('Play Station 5', playStation5Object)

Glen = Person('Glen Veigas', 'glenveigas437@gmail.com', 9619828348)
Vinisha = Person('Vinisha Veigas', 'vinisha.lobo07@gmail.com', 9967080830)
Elvisha = Person('Elvisha Lobo', 'elvishalobo@gmail.com', 9876543210)

playStation5Object.add(Glen.setEmailNotification(playStation5Object))
iPhone14ProPlusObject.add(Vinisha.setSMSNotification(iPhone14ProPlusObject))

iPhone14ProPlusObject.setStockCount(50)
playStation5Object.setStockCount(10)