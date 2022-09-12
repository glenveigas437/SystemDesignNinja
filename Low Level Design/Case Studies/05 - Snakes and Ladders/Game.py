from Board import Board
from Dice import Dice
from Player import Player
from queue import deque


class Game:

    def __init__(self):
        self.players = []
        self.winner = None
    
    def initGame(self, boardSize, noOfSnakes, noOfLadders):
        self.gameBoard = Board(boardSize, noOfSnakes, noOfLadders)
        self.addPlayers()
        self.gameDice = Dice(1)
        self.beginGame()
    

    def addPlayers(self):
        player1 = Player('Glen', 0)
        player2 = Player('Computer', 0)
        self.players.append(player1)
        self.players.append(player2)
    
    def beginGame(self):
        while(self.winner is None):
            playerTurn = self.getPlayerTurn()

            print(f"Current Player is {playerTurn.playerName} and Position is: {playerTurn.playerPosition}")

            currentRoll=self.gameDice.dieCount
            count=0
            while(currentRoll>0):  
                count+=self.gameDice.rollDie()
                currentRoll-=1
            
            currentPosition=self.getnewPosition(count, playerTurn.playerPosition)
            playerTurn.playerPosition = currentPosition

            if playerTurn.playerPosition == (self.gameBoard.boardSize * self.gameBoard.boardSize)-1:
                self.winner = playerTurn
        
        print(f"Winner of the Game is {self.winner.playerName}")


    
    def getPlayerTurn(self):
        currentPlayer = self.players.pop(0)
        self.players.append(currentPlayer)
        return currentPlayer
    

    def getnewPosition(self, count, position):
        newPosition = count + position

        if newPosition > (self.gameBoard.boardSize * self.gameBoard.boardSize)-1:
            return position
        else:
            currentCellFound = self.gameBoard.getCell(newPosition)
            if currentCellFound.jump.start is None:
                print(f"Cell Number is: {newPosition} and it is a normal cell")
                return newPosition
            else:
                if currentCellFound.jump.start>currentCellFound.jump.end:
                    print(f"Bit by Snake going from {currentCellFound.jump.start} to {currentCellFound.jump.end}")
                else:
                    print(f"Lucky!!! Got the ladder Going from {currentCellFound.jump.start} to {currentCellFound.jump.end}")
                return currentCellFound.jump.end





