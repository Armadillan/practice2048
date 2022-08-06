import numpy as np

class Grid:

    def __init__(self, seed=None):
        self.grid = np.zeros((4,4), dtype=np.uint64)
        self._rng = np.random.default_rng(seed)

    def new_tile(self):
        empty = np.argwhere(self.grid == 0)
        new = self._rng.choice(empty, axis=0)
        if self._rng.random() < 0.8:
            self.grid[new[0], new[1]] = 2
        else:
            self.grid[new[0], new[1]] = 4

        return new

    def compress_up(self):
        for x in range(4):
            for y in range(1, 4):
                if self.grid[x, y] != 0:
                    new_y = y
                    while new_y > 0 and self.grid[x, new_y - 1] == 0:
                        new_y -= 1
                    if new_y != y:
                        self.grid[x, new_y] = self.grid[x, y]
                        self.grid[x, y] = 0

    def compress_down(self):
        for x in range(4):
            for y in range(2, -1, -1):
                if self.grid[x, y] != 0:
                    new_y = y
                    while new_y < 3 and self.grid[x, new_y + 1] == 0:
                        new_y += 1
                    if new_y != y:
                        self.grid[x, new_y] = self.grid[x, y]
                        self.grid[x, y] = 0
    
    def compress_left(self):
        for x in range(1, 4):
            for y in range(4):
                if self.grid[x, y] != 0:
                    new_y = y




if __name__ == "__main__":
    grid = Grid()
    print(grid.grid)
    for i in range(2):
        grid.new_tile()
        print(grid.grid)
        grid.compress_up()
        print(grid.grid)
