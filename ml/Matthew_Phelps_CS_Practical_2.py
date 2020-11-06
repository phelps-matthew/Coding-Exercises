""" CS Practical 2 10/14/20 """


class Board:
    def __init__(self, size):
        self.size = size
        self.board = None
        self.make_board()

    def make_board(self):
        arr = [[" "] * self.size for i in range(self.size)]
        self.board = arr

    def print_board(self):
        print(*self.board, sep="\n")

    def add_coin(self, slot, sym):
        """Adds a coin if possible, returns confirmation"""
        # Check if full column
        if self.col_full(slot):
            print("This column is full. Try another one!")
            return False
        else:
            col = self.get_col(slot)
            # Iterate backward in column, looking for empty slot
            for i in reversed(range(self.size)):
                if col[i] == " ":
                    col[i] = sym
                    self.replace_col(slot, col)
                    return True

    def check_win(self, sym):
        # Check columns
        for i in range(self.size):
            if self.check_four(self.get_col(i), sym):
                return True
        # Check rows
        for i in range(self.size):
            if self.check_four(self.get_row(i), sym):
                return True

        # Check diagonal 1
        if self.check_four(self.get_diagonal1(), sym):
            return True

        # Check diagonal 2
        if self.check_four(self.get_diagonal2(), sym):
            return True
        else:
            return False

    def check_four(self, seq, sym):
        if sym * 4 in "".join(seq):
            return True
        else:
            return False

    def col_full(self, col):
        if " " in self.get_col(col):
            return False
        else:
            return True

    def replace_col(self, num, col):
        """Must explicitly replace column with new"""
        for i in range(self.size):
            self.board[i][num] = col[i]

    def get_col(self, col):
        """ Doesn't return view"""
        return [self.board[i][col] for i in range(self.size)]

    def get_row(self, row):
        return self.board[row]

    def get_diagonal1(self):
        return [self.board[i][i] for i in range(self.size)]

    def get_diagonal2(self):
        return [self.board[self.size - 1 - i][i] for i in range(self.size)]

    def get_diagonals(self):
        """Rotate board, pad with zeros"""
        ...


class Game:
    def __init__(self, size):
        self.size = size
        # Initialize players and board
        self.p1 = Player(1, "X", self.size)
        self.p2 = Player(2, "O", self.size)
        self.board = Board(self.size)
        self.board.sym1 = self.p1.sym
        self.board.sym1 = self.p2.sym
        self.count = 0

    def start(self):
        print("Welcome to Connect-Four")
        print("To play, enter a column in [0,{}]".format(self.size-1))
        print("To quit, Ctrl + C")
        self.board.print_board()
        while self.count < self.size ** 2 - 1:
            self.board.add_coin(self.p1.get_input(), self.p1.sym)
            self.board.print_board()
            if self.board.check_win(self.p1.sym):
                print("Player 1 wins!")
                return
            self.board.add_coin(self.p2.get_input(), self.p2.sym)
            self.board.print_board()
            if self.board.check_win(self.p2.sym):
                print("Player 2 wins!")
                return
            self.count += 1
        print("The board is full!")


class Player:
    def __init__(self, num, sym, size):
        self.num = num
        self.sym = sym
        self.size = size

    def get_input(self):
        prompt = "Player" + str(self.num)
        move = input(prompt + ": ")
        cols = [str(i) for i in range(self.size)]
        # Validate input
        if move not in cols:
            print("Illegal move")
            return self.get_input()
        else:
            return int(move)


if __name__ == "__main__":
    try:
        game = Game(4)
        game.start()

    except KeyboardInterrupt:
        print("\nGoodbye")
