#import numpy as np

N = 10

ships = {
         'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2, 'Battleship': 4,
         'Aircraft Carrier': 5
}
ship_abbreviations = {k[0]: k for k in ships}

class Board:
    """Base BB Strat
    """

    def __init__(self):
       """Initialize the board."""
       
       self._ships = set()
       self.board = []
       for i in range(N):
           row = ["_"] * N
           self.board.append(row)

    def show(self):
        """Display the board"""
        header=[chr(ord("A")+i) for i in range(N)]
        print("  " + (" ".join(map(str, range(1,N+1)))))
        for i, row in enumerate(self.board):
            print(header[i], " ".join(row))

    def place(self, ship_type, coord, orientation='horiz'):
        """Add a ship
        """
        
        k = ship_type[0].upper()
        if k in self._ships:
            print("Already added ship!")
        name = ship_abbreviations[k]
        size = ships[name]
        print("Adding ", name)
        row, col = coord
        if orientation == 'horiz':
            if not (0 < col <= N-size) or not (0<row<=N):
                raise ValueError("Invalid coordinate!")
            for j in range(col-1, col+size-1):
                if self.board[row-1][j] != '_':
                    raise ValueError("Ships can't overlap!")
                self.board[row-1][j] = k
        elif orientation == 'vert':
            if not (0 < row <= N-size) or not (0<col<=N):
                raise ValueError("Invalid coordinate!")
            for i in range(row-1, row+size-1):
                if self.board[i][col-1] != '_':
                    raise ValueError("Ships can't overlap!")
                self.board[i][col-1] = k
        else:
            raise ValueError("Invalid Orientation!")
        self._ships.add(k)

    def shot(self, row, col):
        """Add shot"""

        cur = self.board[row-1][col-1]
        if cur in ['x', 'm']:
            raise ValueError("Already guessed!")
        elif cur != '_':
            print("Hit!")
            self.board[row-1][col-1] = 'x'
        else:
            print("Miss ;)")
            self.board[row-1][col-1] = 'm'


if __name__ == "__main__":
    board = Board()
    board.show()
    board.place("A", (1,1))
    board.show()
    board.place("B", (1,6))
    board.place("D", (1,10), orientation='vert')
    board.place("C", (3,10), orientation='vert')
    board.place("S", (6, 10), orientation="vert")
    board.shot(1, 5)
    board.shot(4,4)
    board.show()
