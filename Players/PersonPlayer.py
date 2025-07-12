from .Player import Player
from Move import Move

class PersonPlayer(Player):
    def ValidateUserMove(self, input:str):
        splits = input.split(",")
        if(len(splits) != 2):
            return None
        
        try:
            x = int(splits[0])
            y = int(splits[1])
            return Move(x,y)
        except:
            return None
        
    def DoMove(self):
        while True:
            userInput = input()
            move = self.ValidateUserMove(userInput)
            if move is not None:
                super().PlayMove(move)
                return
            else:
                print("invalid move! e.g. '0,0'")