from Cell import Cell
from Jump import Jump
import random as rd

class Board:
    def __init__(self, boardSize, snakes, ladders):
        self.boardSize = boardSize
        self.gameBoard = self.__buildBoard()
        self.addSL = self.__addSnakesAndLadders(snakes, ladders)
        
    
    def __buildBoard(self):
        self.gameBoard = [[None for i in range(self.boardSize)]for j in range(self.boardSize)]
        
        for row in range(self.boardSize):
            for col in range(self.boardSize):
                newCell = Cell()
                self.gameBoard[row][col]=newCell
        
        return self.gameBoard
    

    def __addSnakesAndLadders(self, snakeCounts, ladderCounts):
        while(snakeCounts>0):
            snakeStart = rd.randint(1, (self.boardSize*self.boardSize)-1)
            snakeEnd = rd.randint(1, (self.boardSize*self.boardSize)-1)
            print(f"Snake Start {snakeStart}, Snake End {snakeEnd}")

            if snakeStart<=snakeEnd:
                continue

            snakeObj = Jump()
            snakeObj.start = snakeStart
            snakeObj.end = snakeEnd

            cell = self.getCell(snakeStart)

            cell = snakeObj

            snakeCounts-=1
        
        
        while(ladderCounts>0):
            ladderStart = rd.randint(1, (self.boardSize*self.boardSize)-1)
            ladderEnd = rd.randint(1, (self.boardSize*self.boardSize)-1)

            if ladderStart>=ladderEnd:
                continue

            ladderObj = Jump()
            ladderObj.start = ladderStart
            ladderObj.end = ladderEnd

            cell = self.getCell(ladderStart)

            cell = ladderObj

            ladderCounts-=1

    def getCell(self, position):
        row = position//self.boardSize
        col = position%self.boardSize

        return self.gameBoard[row][col]