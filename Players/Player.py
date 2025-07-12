from abc import ABC, abstractmethod
import CellValues

class Player(ABC):
    def __init__(self, CellValue: CellValues, game):
        self.CellValue = CellValue
        self.game = game
    
    def PlayMove(self, move):
        validMove = self.game.TestSquareEmpty(move)
        if not validMove:
            print("Invalid Move!")
        else:  
            self.game.PlayerMove(self, move)
        
        return validMove

    @abstractmethod
    def DoMove(self):
        pass