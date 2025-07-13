from Move import Move
from .ComputerPlayerRandom import ComputerPlayerRandom
from .Player import Player
from CellValues import CellValues
from TicTacToeGame import TicTacToeGame

import copy

class ComputerPlayerDefensive(ComputerPlayerRandom):
    def __init__(self, CellValue: CellValues, game, otherPlayer:Player):
        self.otherPlayer = otherPlayer
        super().__init__(CellValue=CellValue, game=game)

    def DoMoveDefensive(self):
        # check all the squares
        # make a new game, and place the opponents move in the spot
        for i in range(self.game.size):
            for j in range(self.game.size):
                if self.game.boardArray[i][j] == CellValues.EMPTY:
                    g2:TicTacToeGame = copy.deepcopy(self.game)
                    move = Move(j,i)
                    # make the other player play the move
                    g2.PlayerMove(self.otherPlayer, move)
                    if g2.IsGameWon():
                        self.game.PlayerMove(self,move)
                        return True
        return False

    def DoMove(self):
        if not self.DoMoveDefensive():
            super().DoMove()