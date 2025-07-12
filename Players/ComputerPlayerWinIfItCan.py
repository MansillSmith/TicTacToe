from Move import Move
from .ComputerPlayerRandom import ComputerPlayerRandom
from CellValues import CellValues
from TicTacToeGame import TicTacToeGame

import copy

class ComputerPlayerWinIfItCan(ComputerPlayerRandom):     

    def DoMove(self):
        # several options here
        # it could check if theres 2 in a row, and add a third.
        # or it could create a new game for all the available moves, and do the move that wins
        for i in range(self.game.size):
            for j in range(self.game.size):
                if self.game.boardArray[i][j] == CellValues.EMPTY:
                    # make a deep copy of the game
                    g2:TicTacToeGame = copy.deepcopy(self.game)
                    move = Move(j,i)
                    g2.PlayerMove(self, move)
                    if g2.IsGameWon():
                        self.game.PlayerMove(self, move)
                        return        
                     
        # if it got here - it couldn't win on the next turn, so just pick a random one 
        super().DoMove()