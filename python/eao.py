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
    
    def _rotate(self, n):
        self.state = np.rot90(self.state, n)

    def _move_up(self) -> Tuple[int, bool]:

        merged = []
        reward = 0
        moved = False
    
        for x in range(4):
            for y in range(1, 4):

                tile_val = self.state[y, x]

                if tile_val:

                    new_y = y

                    while new_y > 0 and self.state[new_y-1, x] == 0:
                        new_y -= 1
                    
                    if new_y > 0  and tile_val == self.state[new_y -1, x] and (new_y - 1, x) not in merged:
                            self.state[y, x] = 0 
                            self.state[new_y-1, x] *= 2
                            merged.append((new_y-1, x))
                            reward += tile_val * 2
                            moved = True

                    elif new_y != y:

                        self.state[y, x] = 0
                        self.state[new_y, x] = tile_val
                        moved = True
        
        return moved, reward

    _rotations = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    }

    def step(self, direction) -> Tuple[np.ndarray, int]:
        if self.gameover:
            return self._reset(), 0
        
        self._rotate(self._rotations[direction])

        moved, reward = self._move_up()

        self._rotate((4 - self._rotations[direction]) % 4)
    
        if moved:
            self._new_tile()
        return self.state, reward

if __name__ == "__main__":
    pass