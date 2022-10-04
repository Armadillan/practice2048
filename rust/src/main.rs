mod cmc;
mod eao;
mod console_frontend;

use crate::console_frontend::Interface;

pub enum Direction {
    Up,
    Right,
    Down,
    Left,
}

trait GameLogic {
    fn reset(&mut self);
    fn step(&mut self, direction: Direction) -> u128;
    fn gameover(&self) -> bool;
}

trait FullGame: GameLogic + console_frontend::Interface {}

impl Interface for cmc::Grid {
    fn score(&self) -> u128 {
        self.score
    }
    fn get_grid_val(&self, x: usize, y: usize) -> u128 {
        self.grid[x][y]
    }
}

impl Interface for eao::Grid {
    fn score(&self) -> u128 {
        self.score
    }
    fn get_grid_val(&self, x: usize, y: usize) -> u128 {
        self.grid[x][y]
    }
}

impl FullGame for cmc::Grid {}
impl FullGame for eao::Grid {}

fn game_loop(game: &mut impl FullGame) {
    game.reset();
    let mut input: Direction;
    loop {
        game.pprint();
        input = game.get_input();
        game.step(input);
        if game.gameover()  {
            if !game.handle_gameover() {
                break
            }
            game.reset();
        }
    }
}

fn main() {


    // let mut grid = cmc::Grid::new();
    let mut grid = eao::Grid::new();
    game_loop(&mut grid);
}
