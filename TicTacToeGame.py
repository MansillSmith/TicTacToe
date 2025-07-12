from CellValues import CellValues
import Move
from Players import Player

class TicTacToeGame:    
    def __init__(self, size):
        self.size = size
        self.boardArray = [[CellValues.EMPTY for _ in range(size)] for _ in range(size)]
        self.moveCount = 0
    
    def __str__(self):
        outputString = "\n"
        for i in range(self.size):
            outputString += '|'.join(str(item) for item in self.boardArray[i]) + '\n'
            if i != self.size -1:
                outputString += '-'*((self.size*2)-1) + '\n'
        return outputString
    
    def TestSquareEmpty(self, move:Move):
        return self.boardArray[move.y][move.x] == CellValues.EMPTY        
    
    def PlayerMove(self, Player:Player, move:Move):
        self.boardArray[move.y][move.x] = Player.CellValue
        self.moveCount += 1

    def IsBoardFull(self):
        return self.moveCount >= self.size**self.size

    def IsGameWon(self):
        def CheckValidWinList(array):
            return array[0] != CellValues.EMPTY and all(x == array[0] for x in array)

        def CheckRows(self):
            for i in range(self.size):
                if CheckValidWinList(self.boardArray[i]):
                    return True
            return False

        def CheckColumns(self):
            # for each row
            for i in range(self.size):
                # for each column
                tempArray = []
                for j in range(self.size):
                    tempArray.append(self.boardArray[j][i])
                
                if CheckValidWinList(tempArray):
                    return True
            return False
        
        def CheckDiagonals(self):
            for j in range(2):
                tempArray = []
                for i in range(self.size):
                    if j == 0:
                        tempArray.append(self.boardArray[i][i])
                    elif j == 1:
                        tempArray.append(self.boardArray[i][self.size-i-1])
                if CheckValidWinList(tempArray):
                    return True
            return False
        
        return CheckRows(self) or CheckColumns(self) or CheckDiagonals(self)