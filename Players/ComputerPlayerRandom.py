from Move import Move
from .Player import Player
import random

class ComputerPlayerRandom(Player):
    def DoMove(self):
        while True:
            move = Move(random.randint(0,self.game.size-1),random.randint(0,self.game.size-1))
            if super().PlayMove(move):                
                return    