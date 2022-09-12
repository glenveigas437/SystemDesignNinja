import random
class Dice:
    def __init__(self, dieCount):
        self.dieCount=dieCount
    
    def rollDie(self):
        return random.randint(1, 6)
        
        
