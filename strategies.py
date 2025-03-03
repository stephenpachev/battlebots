import random
from board import Board, N

class RandomStrat:
    """Base random strategy."""

    def __init__(self):
        """Randomly initialize the board with ships."""

        self.ship_board = Board()
        self.shot_board = Board()

        for ship in ["A", "B", "C", "S", "D"]:
            coord, orientation = self.choose_placement()
            while not self.ship_board.place(ship, coord, orientation):
                coord, orientation = self.choose_placement()
        print("Placed ships.")
        self.ship_board.show()

    def choose_placement(self):
        """Choose random ship placement."""
        
        orientation = random.choice(["horiz", "vert"])
        return (random.randint(1, N+1), random.randint(1,N+1)), orientation


strats = {'random': RandomStrat}

def make_strat(name):
    """Initialize a strategy."""

    if name not in strats:
        raise NotImplementedError(f"Strategy '{name}' not yet implemented!")
    return strats[name]()
