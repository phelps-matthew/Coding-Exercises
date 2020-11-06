import random


""" Tic Tac Toe Game from CodeSignal Practical #1. 10/13/2020 """


class TicTacToe:
    def __init__(self):
        """Initialize with empty board"""
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.move_count = 0
        self.agent = False

    def make_move(self, loc: list, mark: str) -> str:
        """Take in location [r,c] and mark 'X' or 'O', validating input"""
        r, c = loc[0], loc[1]
        if self.board[r][c] == " ":
            self.board[r][c] = mark
            self.check_winner()
            self.move_count += 1
            return
        else:
            print("Invalid location for mark")
            return

    def check_winner(self):
        for row in range(3):
            # check rows
            if self.board[row] == ["X", "X", "X"]:
                return "X"
            if self.board[row] == ["O", "O", "O"]:
                return "O"

        # check cols
        for col in range(3):
            column = [self.board[row][col] for row in range(3)]
            if column == ["X", "X", "X"]:
                return "X"
            if column == ["O", "O", "O"]:
                return "O"

        # check diagonal
        diag = [self.board[row][row] for row in range(3)]
        if diag == ["X", "X", "X"]:
            return "X"
        if diag == ["O", "O", "O"]:
            return "O"

    def get_input(self):
        """Get user move"""
        try:
            r, c, mark = input("Enter move: ").split()
            if r not in ["0", "1", "2"]:
                print("Row must be an integer")
                return self.get_input()
            if c not in ["0", "1", "2"]:
                print("Column must be an integer")
                return self.get_input()
            if mark != "O" and mark != "X":
                print("Invalid mark, must be 'X' or 'O'")
                return self.get_input()
            return [int(r), int(c)], mark
        # Improper number of inputs
        except ValueError:
            print("Invalid input format")
            return self.get_input()

    def print_board(self):
        """Display board"""
        print(*self.board, sep="\n")

    def play_game(self):
        """Play the game?"""
        print("Welcome to Tic Tac Toe!")
        print(" Input format: 'r c mark', with r, c in [0,2] and mark in ['X','O'].")
        print(" Ctrl + C to exit.")
        print("-" * 15)
        print("Here we go!")
        print("-" * 15)

        while self.move_count < 9:
            self.print_board()
            if self.agent:
                if self.move_count % 2 == 0:
                    r = random.randrange(0, 3)
                    c = random.randrange(0, 3)
                    m = random.randrange(0, 2)
                    self.make_move([r, c], ["O", "X"][m])
            loc, mark = self.get_input()
            self.make_move(loc, mark)
            outcome = self.check_winner()
            if outcome == "X":
                self.print_board()
                print("X wins!")
                return
            if outcome == "O":
                self.print_board()
                print("O wins!")
                return
        print("Tie game ^_^")

    def play_agent(self):
        self.agent = True


if __name__ == "__main__":
    try:
        game = TicTacToe()
        game.play_game()
    except KeyboardInterrupt:
        print("\nGoodbye.")
        exit()
