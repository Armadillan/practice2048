enum Direction {
    Up,
    Right,
    Down,
    Left,
}

export class Game {
    grid: Array<Array<number>>;

    private new_tile() {

        // find all empty tiles
        let empty = new Array<[number, number]>();
        for (let y = 0; y < 4; y++) {
            for (let x = 0; x < 4; x++) {
                if (this.grid[x][y] === 0) {
                    empty.push([x, y]);
                }
            }
        }
        
        // choose one
        let new_tile: [number, number] = empty[Math.floor(Math.random() * empty.length)];

        // decide if 2 or 4
        let new_val = 2;
        if (Math.random() > 0.8) {
            new_val = 4;
        }

        // set new value
        this.grid[new_tile[0]][new_tile[1]] = new_val;

    }

    reset() {
        this.grid = Array.from(Array(4), () => Array(4).fill(0))
        this.new_tile();
        this.new_tile();
    }

    private rotate_90() {
        this.grid = Array(4).fill(0).map((val, index) => this.grid.map(row => row[index]).reverse())
    }

    rotate(n: number) {
        for (let i = 0; i < n; i++) {
            this.rotate_90();
        }
    }
}

let game = new Game;
console.log(game.grid);
game.reset();
console.log(game.grid);
game.rotate(2);
console.log(game.grid);
console.log(Math.random())
