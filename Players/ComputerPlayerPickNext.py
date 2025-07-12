import Player
import CellValues
from Move import Move

class ComputerPlayerPickNext(Player):
    def DoMove(self):
        for i in range(self.game.size):
            for j in range(self.game.size):
                if self.game.boardArray[i][j] == CellValues.EMPTY:
                    super().PlayMove(Move(j,i))
                    return