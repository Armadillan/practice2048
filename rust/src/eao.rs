use rand::seq::SliceRandom;
use rand::Rng;

use crate::Direction as Direction;
use crate::GameLogic as GameLogic;

pub struct Grid {
    pub grid: [[u128; 4]; 4],
    pub score: u128,
}

impl Grid {

    pub fn new() -> Self {
        Self {
            grid: [[0; 4]; 4],
            score: 0,
        }
    }

    fn new_tile(&mut self) {
        let mut empty: Vec<(usize, usize)> = Vec::new();
        for y in 0..4 {
            for x in 0..4 {
                if self.grid[x][y] == 0 {
                    empty.push((x, y));
                }
            }
        }

        let new_tile = empty.choose(&mut rand::thread_rng())
            .expect("there should be empty tiles after a valid move");

        let mut new_val: u128 = 2;
        if rand::thread_rng().gen::<f64>() > 0.8 {
            new_val = 4;
        }

        self.grid[new_tile.0][new_tile.1] = new_val;
    }

    fn rotate_90(&mut self) {
        self.grid = [0, 1, 2, 3]
            .map(|index| {
                let mut tmp = self.grid.map(|row| row[index]);
                tmp.reverse();
                tmp
                }
            );
    }

    fn rotate(&mut self, n: usize) {
        for _ in 0..n {
            self.rotate_90()
        }
    }

    fn r#move(&mut self, direction: Direction) -> (bool, u128) {
        let mut moved = false;
        let mut reward = 0;
        let mut merged: Vec<(usize, usize)> = Vec::new();

        let rotate_num = match direction {
            Direction::Up => 3,
            Direction::Right => 2,
            Direction::Down => 1,
            Direction::Left => 0,
        };

        self.rotate(rotate_num);

        for x in 0..4 {
            for y in 1..4 {
                let tile_val = self.grid[x][y];
                if tile_val > 0 {
                    let mut new_y = y;

                    while new_y > 0 && self.grid[x][new_y-1] == 0 {
                        new_y -= 1;
                    }

                    if new_y > 0
                        && tile_val == self.grid[x][new_y-1]
                        && !merged.contains(&(x, new_y-1)) {
                            self.grid[x][y] = 0;
                            self.grid[x][new_y-1] *= 2;
                            merged.push((x, new_y-1));
                            reward += tile_val * 2;
                            moved = true;
                    } else if new_y != y {
                        self.grid[x][y] = 0;
                        self.grid[x][new_y] = tile_val;
                        moved = true;
                    }
                }
            }
        }

        self.rotate((4 - rotate_num) % 4);

        return (moved, reward);
    }
}

impl GameLogic for Grid {

    fn reset(&mut self) {
        self.grid = [[0;4];4];
        self.new_tile();
        self.new_tile();
        self.score = 0;
    }

    fn step(&mut self, direction: Direction) -> u128 {

        if self.gameover() {
            self.reset();
            return 0;
        }

        let (moved, reward) = self.r#move(direction);

        if moved {
            self.new_tile();
        }

        self.score += reward;

        return reward;
    }

    fn gameover(&self) -> bool {
        // available empty tiles
        for row in self.grid {
            for val in row {
                if val == 0 {
                    return false
                }
            }
        }
        // available vertical merges
        for y in 0..3 {
            for x in 0..4 {
                if self.grid[x][y] == self.grid[x][y+1] {
                    return false;
                }
            }
        }
        // available horizontal merges
        for y in 0..4 {
            for x in 0..3 {
                if self.grid[x][y] == self.grid[x+1][y] {
                    return false;
                }
            }
        }

        return true;
    }
}
