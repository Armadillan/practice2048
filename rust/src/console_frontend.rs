use std::io;

use crate::Direction as Direction;

pub trait Interface {

    fn score(&self) -> u128;
    fn grid(&self) -> [[u128;4];4];

    fn get_str_val(&self, x: usize, y: usize) -> String {
        format!("{: ^7}", self.grid()[x][y])
    }
    fn pprint(&self) {
        println!("|-------|-------|-------|-------|");
        println!("|{}|{}|{}|{}|",
        self.get_str_val(0,0), self.get_str_val(0,1),
        self.get_str_val(0,2), self.get_str_val(0,3)
        );
        println!("|-------|-------|-------|-------|");
        println!("|{}|{}|{}|{}|",
        self.get_str_val(1,0), self.get_str_val(1,1),
        self.get_str_val(1,2), self.get_str_val(1,3)
        );
        println!("|-------|-------|-------|-------|");
        println!("|{}|{}|{}|{}|",
        self.get_str_val(2,0), self.get_str_val(2,1),
        self.get_str_val(2,2), self.get_str_val(2,3)
        );
        println!("|-------|-------|-------|-------|");
        println!("|{}|{}|{}|{}|",
        self.get_str_val(3,0), self.get_str_val(3,1),
        self.get_str_val(3,2), self.get_str_val(3,3)
        );
        println!("|-------|-------|-------|-------|");
        println!("Score: {}", self.score());
        }

    fn get_input(&mut self) -> Direction {
        let mut input = String::new();

        while !["w\n", "a\n", "s\n", "d\n"].contains(&input.as_str()) {
            input = String::from("");
            io::stdin()
                .read_line(&mut input)
                .expect("Failed to read line");
        }

        match input.as_str() {
            "w\n" => Direction::Up,
            "a\n" => Direction::Left,
            "s\n" => Direction::Down,
            "d\n" => Direction::Right,
            _ => panic!("input should be one of wasd")

        }

    }
    fn handle_gameover(&self) -> bool {
        self.pprint();
        println!("Game over!");
        let mut answer = String::new();
        println!("Restart? [Y/n]");

        io::stdin()
            .read_line(&mut answer)
            .expect("Failed to read line");

        if ["no\n", "n\n"].contains(&answer.to_lowercase().as_str()) {
            return false
        };

        return true
    }
}
