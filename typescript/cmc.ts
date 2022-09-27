export enum Direction {
    // also number of rotations to get each direction
    Up = 3,
    Right = 2,
    Down = 1,
    Left = 0,
}

export class Game {
    grid: Array<Array<number>>;
    score: number;

    constructor() {
        this.reset();
    }

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
        let new_tile: [number, number] =
            empty[Math.floor(Math.random() * empty.length)];

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
        this.score = 0;
    }

    private rotate_90() {
        this.grid = Array(4)
        .fill(0)
        .map((val, index) => this.grid.map(row => row[index]).reverse())
    }

    private rotate(n: number) {
        for (let i = 0; i < n; i++) {
            this.rotate_90();
        }
    }

    private compress(): boolean {

        let moved: boolean = false;

        for (let x = 0; x < 4; x++) {
            for (let y = 1; y < 4; y++) {

                if (this.grid[x][y] > 0) {
                    let new_y = y;

                    while (new_y > 0 && this.grid[x][new_y -1] === 0) {
                        new_y--;
                    }

                    if (new_y !== y) {
                        this.grid[x][new_y] = this.grid[x][y];
                        this.grid[x][y] = 0;
                        moved = true;
                    }
                }
            }
        }
        return moved;
    }

    private merge(): number {
        let reward = 0;

        for (let x = 0; x < 4; x++) {
            for (let y = 0; y < 3; y++) {

                if (this.grid[x][y] > 0) {
                    if (this.grid[x][y] == this.grid[x][y+1]) {
                        this.grid[x][y+1] = 0;
                        this.grid[x][y] *= 2;
                        reward += this.grid[x][y];
                    }
                }
            }
        }
        return reward;
    }

    private move(direction: Direction): [boolean, number] {
        let moved = false;

        this.rotate(direction);

        moved = this.compress();
        let reward = this.merge();
        moved = this.compress() || moved || reward > 0;

        this.rotate((4 - direction) % 4);

        return [moved, reward]

    }

    step(direction: Direction): number {
        if (this.gameover) {
            this.reset();
            return 0;
        }

        let [moved, reward] = this.move(direction);

        if (moved) {
            this.new_tile();
        }

        this.score += reward;
        return reward
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
if (require.main === module) {
    let game = new Game;
    console.log(game.grid);
    game.reset();
    console.log(game.grid);
    game.step(Direction.Up);
    console.log(game.gameover)
    console.log(game.grid);
    console.log(Math.random())
}
