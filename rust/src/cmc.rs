
use rand::seq::SliceRandom;
use rand::Rng;

pub enum Direction {
    Up,
    Right,
    Down,
    Left,
}

pub struct Grid {
    pub grid: [[u128; 4]; 4],
    pub score: u128,
}

pub fn empty_grid() -> Grid {
    Grid {
        grid: [[0; 4]; 4],
        score: 0,
    }
}

impl Grid {
    pub fn reset(&mut self) {
        self.grid = [[0;4];4];
        self.new_tile();
        self.new_tile();
        self.score = 0;
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
        todo!();
    }

    fn rotate(&mut self, n: usize) {
        for _ in 0..n {
            self.rotate_90()
        }
    }

    fn compress(&mut self) -> bool {
        let moved = false;
        todo!();
        return moved;
    }

    fn merge(&mut self) -> u128 {
        let reward = 0;
        todo!();
        return reward;
    }

    fn r#move(&mut self, direction: Direction) -> (bool, u128) {

        let rotate_num = match direction {
            Direction::Up => 3,
            Direction::Right => 2,
            Direction::Down => 1,
            Direction::Left => 0,
        };
        self.rotate(rotate_num);

        let mut moved = self.compress();
        let reward = self.merge();
        moved = self.compress() || moved || reward > 0;

        self.rotate((4 - rotate_num) % 4);

        return (moved, reward);
    }

    pub fn step(&mut self, direction: Direction) -> u128 {

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

    pub fn gameover(&mut self) -> bool {
        todo!()
    }
}
