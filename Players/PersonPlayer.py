from .Player import Player
from Move import Move
from CellValues import CellValues

class PersonPlayer(Player):
    def ValidateUserMove(self, input:str):
        splits = input.split(",")
        if(len(splits) != 2):
            return None
        
        try:
            x = int(splits[0])
            y = int(splits[1])

            if x >= 0 and x <= (self.game.size-1) and y >=0 and y <= (self.game.size-1):
                return Move(x,y)
        except:
            pass

        return None
        
    def DoMove(self):
        while True:
            userInput = input()
            move = self.ValidateUserMove(userInput)
            if move is not None and self.game.boardArray[move.y][move.x] == CellValues.EMPTY:
                super().PlayMove(move)
                return
            else:
                print("invalid move! e.g. '0,0'")