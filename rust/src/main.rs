mod cmc;
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

impl FullGame for cmc::Grid {}

fn game_loop(game: &mut dyn FullGame) {
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

    let mut grid = cmc::Grid::new();
    game_loop(&mut grid);

    // let mut test_grid = cmc::Grid::new();
    // test_grid.reset();
    // test_grid.step(Direction::Right);
    // test_grid.pprint();
    // impl console_frontend::Interface for cmc::Grid{
    //     fn score(&self) -> u128 {
    //         self.score
    //     }
    //     fn grid(&self) -> [[u128;4];4] {
    //         self.grid
    //     }
    // }
    // test_grid.get_input();
}
