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

    def reset(self):
        self.__init__()
        self.new_tile()
        self.new_tile()

    def rotate(self, n):
        self.grid = np.rot90(grid, n)

    def compress(self):
        #down
        for x in range(4):
            for y in range(1, 4):
                #if not 0
                if self.grid[x, y]:
                    new_y = y
                    while new_y > 0 and self.grid[x, new_y - 1] == 0:
                        new_y -= 1
                    if new_y != y:
                        self.grid[x, new_y] = self.grid[x, y]
                        self.grid[x, y] = 0

    def merge(self):
        for x in range(4):
            for y in range(0, 3):
                #if not 0
                if self.grid[x, y]:
                    if self.grid[x, y] == self.grid[x, y + 1]:
                        self.grid[x, y + 1] = 0
                        self.grid[x, y] *= 2

    rotations = {
        0: 2,
        1: 1,
        2: 0,
        3: 3,
    }

    def move(self, direction):
        """
        directins:
        0 - up
        1 - right
        2 - down
        3- left
        """
        self.rotate(roations[direction])
        self.compress()
        self.merge()
        self.compress()
        self.rotate((4 - direction) % 4)

        #todo
        #generate new tiles and check for gameover

    #property for compatibility with existing frontent
    @property
    def check_gameover(self):

        if not self.state.all():
            return False

        for y in range(3):
            for x in range(4):
                if self.state[y, x] == self.state[y+1, x]:
                    return False
        for y in range(4):
            for x in range(3):
                if self.state[y, x] == self.state[y, x+1]:
                    return False
        return True

    #for compatibility with existing frontent
    self.step = self.move
    self.state = self.grid

    def pprint(self):
        # 7x7 chars for grid squares
        #todo
        pass



if __name__ == "__main__":
    grid = Grid()
    for i in range(2):
        grid.new_tile()
        grid.new_tile()
    print(grid.grid)
    grid.compress()
    # grid.rotate(2)
    print(grid.grid)
