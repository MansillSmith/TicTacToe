from enum import Enum

class CellValues(Enum):
    EMPTY = (0,' ')
    NOUGHT = (1, 'O')
    CROSS = (2, 'X')

    def __init__(self, number, symbol: str):
        self.number = number
        self.symbol: str = symbol
    
    def __str__(self):
        return str(self.symbol)