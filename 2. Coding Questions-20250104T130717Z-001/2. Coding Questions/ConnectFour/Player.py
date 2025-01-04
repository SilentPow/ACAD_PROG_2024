class Board:
    grid = []
    COLUMNS = 7
    HEIGHT = 6

class Player:
    def __init__(self, id):
        self.id = id
    
    def DoMove(self, board) -> int:
        if board.grid[0][0] == self.id:
            return 0
        else:
            return -1
