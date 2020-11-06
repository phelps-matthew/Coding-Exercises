import random
import string
import string
import re
import numpy as np
import time

words = string.ascii_lowercase


class board:
    def __init__(self, n_grid=9):
        self.n_grid = n_grid
        self.cur = [[" " for _ in range(self.n_grid)] for _ in range(self.n_grid)]

    def __repr__(self):
        # structured print for the board
        res = ""
        for i in range(2 * (self.n_grid + 1)):
            if i == 0:
                res += " " * 6
                res += "   ".join(words[: self.n_grid])
                res += " " * 2
                res += "\n"
                continue
            if i % 2 == 1:
                res += " " * 4 + "-" * (4 * self.n_grid + 1) + "\n"
                continue
            res += (
                str(i // 2)
                + " " * (4 - len(str(i // 2)))
                + "| "
                + " | ".join(self.cur[(i - 1) // 2])
                + " |\n"
            )
        return res


class game(board):
    def __init__(self, n_mines=10, n_grid=9):
        self.mine_map = board(n_grid)  # mine board
        self.dis_map = board(n_grid)  # display board
        self.n_mines = n_mines
        self.n_grid = n_grid
        # randomly initialize the mine positions (r,c) int coordinates
        self.pos_mines = list(
            map(
                lambda x: divmod(x, self.n_grid),
                np.random.choice(self.n_grid ** 2, self.n_mines, replace=False),
            )
        )
        for x, y in self.pos_mines:
            self.mine_map.cur[x][y] = "*"

    def is_cell(self, x, y):
        return 0 <= x < self.n_grid and 0 <= y < self.n_grid

    def is_mine(self, x, y):
        return self.mine_map.cur[x][y] == "*"

    def get_neighbor_cnt(self, x, y, val):
        cnt = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.is_cell(x + i, y + j):
                    if (i, j) != (0, 0):
                        if self.mine_map.cur[x + i][y + j] == val:
                            cnt += 1
        return cnt

    def get_neighbor_locs(self, x, y, val="0"):
        out = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.is_cell(x + i, y + j):
                    if (i, j) != (0, 0):
                        if self.mine_map.cur[x + i][y + j] == val:
                            out.append((x + i, y + j))
        return out

    def get_zeros(self, x, y):
        """Get all zeros connect to (x,y)"""
        return self._get_subzeros(x, y)

    def _get_subzeros(self, x, y, zset=set()):
        """Helper function to recursively gather connected zeros"""
        if (x, y) in zset:  # No new zeros
            return
        zset.add((x, y))
        zeros = {*self.get_neighbor_locs(x, y)}
        for z in zeros:
            self._get_subzeros(*z, zset=zset)
        return zset

    def mark_proximities(self):
        for i in range(self.n_grid):
            for j in range(self.n_grid):
                if not self.is_mine(i, j) and self.is_cell(i, j):
                    self.mine_map.cur[i][j] = str(self.get_neighbor_cnt(i, j, "*"))

    def reveal_zeros(self, x, y):
        zeros = self.get_zeros(x, y)
        for x, y in zeros:
            self.dis_map.cur[x][y] = '0'

    def play(self):
        """
        Play the game
        """
        print("=" * 70)
        print(
            "Starting Minesweeper (with {} mines on {}x{} grid.)".format(
                self.n_mines, self.n_grid, self.n_grid
            )
            + "\n"
        )
        print(self.dis_map)
        print("=" * 70)


if __name__ == "__main__":
    g = game(10, 9)  # n_mines=10, n_grid=9
    g.play()
    print(g.mine_map)
    g.mark_proximities()
    print(g.mine_map)
    print(g.dis_map)
    x,y = map(int, input("Enter coordinates:").split())
    g.reveal_zeros(x, y)
    print(g.mine_map)
    print(g.dis_map)
