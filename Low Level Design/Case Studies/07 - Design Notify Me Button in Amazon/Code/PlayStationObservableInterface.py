from ObservableInterface import ObservableInterface

class PlayStation5ObservableInterface(ObservableInterface):
    productName = 'Play Station 5'
    def __init__(self):
        self.observerList = []
        self.stockCount = 0

    def add(self, observer):
        self.observerList.append(observer)
    
    def remove(self, observer):
        indexOfObserver = self.observerList.index(observer)
        self.observerList.pop(indexOfObserver)
    
    def notifySubscribers(self):
        for observer in self.observerList:
            observer.update()
    
    def setStockCount(self, newStockAdded):
        if self.stockCount==0:
            self.stockCount+=newStockAdded
            self.notifySubscribers()
    
    def getStockCount(self):
        return self.stockCount