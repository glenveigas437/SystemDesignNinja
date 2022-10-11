from abc import ABC, abstractmethod

class ObservableInterface(ABC):
    @abstractmethod
    def add(self, observerInterfaceObject):
        pass
    
    @abstractmethod
    def remove(self, observerInterfaceObject):
        pass
    
    @abstractmethod
    def notifySubscribers(self):
        pass
    
    def setStockCount(self, newStockAdded):
        pass

    def getStockCount(self):
        pass