mod cmc;

fn main() {
    let mut test_grid = cmc::empty_grid();
    test_grid.reset();
    test_grid.step(cmc::Direction::Right);
    println!("{:?}", test_grid.grid);
}
