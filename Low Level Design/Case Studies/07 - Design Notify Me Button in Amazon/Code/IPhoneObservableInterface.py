from ObservableInterface import ObservableInterface

class IphoneObservableInterface(ObservableInterface):
    productName = 'iPhone 14 Pro Plus'
    def __init__(self):
        self.observerList = []
        self.stockCount = 0

    def add(self, observer):
        self.observerList.append(observer)
    
    def remove(self, observer):
        indexOfObserver = self.observerList.index(observer)
        self.observerList.pop(indexOfObserver)
    
    def notifySubscribers(self):
        for observers in self.observerList:
            observers.update()
    
    def setStockCount(self, newStockAdded):
        if self.stockCount==0:
            self.stockCount+=newStockAdded
            self.notifySubscribers()

    
    def getStockCount(self):
        return self.stockCount