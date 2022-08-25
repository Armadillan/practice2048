import numpy as np

class Game:

    def __init__(self, seed=None):
        self.state = np.zeros((4,4), dtype=np.uint64)
        self._rng = np.random.default_rng(seed)

    def new_tile(self):
        empty = np.argwhere(self.state == 0)
        new = self._rng.choice(empty, axis=0)
        if self._rng.random() < 0.8:
            self.state[new[0], new[1]] = 2
        else:
            self.state[new[0], new[1]] = 4

        return new

    def reset(self):
        self.__init__()
        self.new_tile()
        self.new_tile()
        return self.state

    def rotate(self, n):
        self.state = np.rot90(self.state, n)

    def compress(self):
        #up
        moved = False

        for x in range(4):
            for y in range(1, 4):
                #if not 0
                if self.state[y, x]:
                    new_y = y
                    while new_y > 0 and self.state[new_y - 1, x] == 0:
                        new_y -= 1
                    if new_y != y:
                        self.state[new_y, x] = self.state[y, x]
                        self.state[y, x] = 0
                        moved = True
        return moved

    def merge(self):
        reward = 0
        for x in range(4):
            for y in range(0, 3):
                #if not 0
                if self.state[y, x]:
                    if self.state[y, x] == self.state[y + 1, x]:
                        self.state[y + 1, x] = 0
                        self.state[y, x] *= 2
                        reward += self.state[y, x]
                        moved = True
        return reward

    rotations = {
        0: 0,
        1: 1,
        2: 2,
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
        moved = False

        self.rotate(self.rotations[direction])

        moved = self.compress()

        reward = self.merge()
        moved = moved or reward
        
        #or operator is short-circuit
        moved = self.compress() or moved

        self.rotate((4 - self.rotations[direction]) % 4)

        return moved, reward


    def step(self, direction) -> (np.ndarray, int):
        # move + generate tiles and check gameover

        # frontend should check this property ad give option to restart
        # to restart, simply call this function again
        if self.gameover:
            return self.reset(), 0

        moved, reward = self.move(direction)
        if moved:
            self.new_tile()

        return self.state, reward

    #property for compatibility with existing frontent
    @property
    def gameover(self):

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

if __name__ == "__main__":
    game = Game()
    for i in range(2):
        game.new_tile()
        game.new_tile()
    print(game.state)
    game.compress()
    # grid.rotate(2)
    print(game.state)
