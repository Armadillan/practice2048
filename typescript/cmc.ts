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

    private rotate(n: number) {
        for (let i = 0; i < n; i++) {
            this.rotate_90();
        }
    }

    private compress() {
        //TODO
    }

    private merge() {
        //TODO
    }

    private move(direction: Direction) {
        //TODO
    }

    step(direction: Direction) {
        //TODO
    }

    get gameover(): boolean {

        // available empty tiles
        for (let row of this.grid) {
            for (let val of row) {
                if (val === 0) {
                    return false
                }
            }
        }

        // available vertical merges
        for (let y = 0; y < 3; y++) {
            for (let x = 0; x < 4; x++) {
                if (this.grid[x][y] === this.grid[x][y+1]) {
                    return false
                }
            }
        }

        //available horizontal merges
        for (let y = 0; y < 4; y++) {
            for (let x = 0; x < 3; x++) {
                if (this.grid[x][y] === this.grid[x+1][y]) {
                    return false
                }
            }
        }
        
        return true
    }
}

let game = new Game;
console.log(game.grid);
game.reset();
console.log(game.grid);
// game.rotate(2);
console.log(game.gameover)
console.log(game.grid);
console.log(Math.random())
