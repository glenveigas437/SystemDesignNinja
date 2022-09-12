from Game import Game

class Main:
    def playGame(self):
        self.startGame()
    
    def startGame(self):
        Game().initGame(10, 5, 5)

Main().playGame()