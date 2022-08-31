import numpy as np
from typing import Tuple

class Game:

    def __init__(self, seed=None):
        self.state = np.zeros((4,4), dtype=np.uint64)
        self._rng = np.random.default_rng(seed)

    def _new_tile(self):
        empty = np.argwhere(self.state == 0)
        new = self._rng.choice(empty, axis=0)
        if self._rng.random() < 0.8:
            self.state[new[0], new[1]] = 2
        else:
            self.state[new[0], new[1]] = 4

        return new

    def reset(self):
        self.__init__()
        self._new_tile()
        self._new_tile()
        return self.state

    def _rotate(self, n):
        self.state = np.rot90(self.state, n)

    def _compress(self):
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

    def _merge(self):
        reward = 0
        for x in range(4):
            for y in range(3):
                #if not 0
                if self.state[y, x]:
                    if self.state[y, x] == self.state[y + 1, x]:
                        self.state[y + 1, x] = 0
                        self.state[y, x] *= 2
                        reward += int(self.state[y, x])
        return reward

    def _move(self, direction):
        """
        directions:
        0 - up
        1 - right
        2 - down
        3- left
        """
        moved = False

        self._rotate(direction)

        moved = self._compress()

        reward = self._merge()
        moved = moved or reward
        
        #or operator is short-circuit
        moved = self._compress() or moved

        self._rotate((4 - direction) % 4)
        return moved, reward


    def step(self, direction) -> Tuple[np.ndarray, int]:
        # move + generate tiles and check gameover

        # frontend should check this property ad give option to restart
        # to restart, simply call this function again
        if self.gameover:
            return self._reset(), 0

        moved, reward = self._move(direction)
        if moved:
            self._new_tile()
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
        game._new_tile()
        game._new_tile()
    print(game.state)
    game._compress()
    # grid.rotate(2)
    print(game.state)
