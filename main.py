import os
from TicTacToeGame import TicTacToeGame
from Players.PersonPlayer import PersonPlayer
from Players.ComputerPlayerRandom import ComputerPlayerRandom
from Players.ComputerPlayerWinIfItCan import ComputerPlayerWinIfItCan
from Players.ComputerPlayerDefensive import ComputerPlayerDefensive
from Players.ComputerPlayerOffensiveAndDefensive import ComputerPlayerOffensiveAndDefensive
from CellValues import CellValues

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


game = TicTacToeGame(3)
print(game)

# players = [PersonPlayer(CellValues.NOUGHT, game), ComputerPlayerPickNext(CellValues.CROSS, game)]
# players = [PersonPlayer(CellValues.NOUGHT, game), ComputerPlayerRandom(CellValues.CROSS, game)]
# players = [PersonPlayer(CellValues.NOUGHT, game), ComputerPlayerWinIfItCan(CellValues.CROSS, game)]

p1 = PersonPlayer(CellValues.NOUGHT, game)
# players = [p1, ComputerPlayerDefensive(CellValues.CROSS, game, p1)]
players = [ComputerPlayerOffensiveAndDefensive(CellValues.CROSS, game, p1), p1]
turnNumber = 0
while not game.IsGameWon() and not game.IsBoardFull():
    players[turnNumber % len(players)].DoMove()
    clear_terminal()
    print(game)
    turnNumber += 1

            
print("Game Over!")