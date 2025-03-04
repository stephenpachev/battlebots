from board import Board
import strategies as strats

class Game:
    """Interface for playing game."""

    def __init__(self, strat='random'):
        """Initialize game."""

        self.strat = strats.make_strat(strat)


if __name__ == "__main__":
    game = Game()

