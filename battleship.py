import numpy as np

N = 10

class BBBot:
    """Base BB Strat
    """

    def __init__(self):
       """Initialize the board."""
       
       self.board = np.zeros((N, N), dtype=np.int8)
       print(self.board)


if __name__ == "__main__":
    board = BBBot()
    
