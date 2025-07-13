from Move import Move
from .ComputerPlayerRandom import ComputerPlayerRandom
from .ComputerPlayerWinIfItCan import ComputerPlayerWinIfItCan
from .ComputerPlayerDefensive import ComputerPlayerDefensive
from .Player import Player
from CellValues import CellValues
from TicTacToeGame import TicTacToeGame

class ComputerPlayerOffensiveAndDefensive(ComputerPlayerRandom):
    def __init__(self, CellValue: CellValues, game, otherPlayer:Player):
        self.offensivePlayer = ComputerPlayerWinIfItCan(CellValue, game)
        self.defensivePlayer = ComputerPlayerDefensive(CellValue, game, otherPlayer)
        super().__init__(CellValue, game)

    def DoMove(self):
        # check if it can win
        if not self.offensivePlayer.DoMoveIfCanWin():
            # if it can't win - do a defensive move
            if not self.defensivePlayer.DoMoveDefensive():
                super().DoMove()