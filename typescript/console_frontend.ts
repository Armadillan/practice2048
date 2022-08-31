import * as readline from "readline";

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const question = (questionText: string) =>
    new Promise<string>(resolve => rl.question(questionText, resolve));

interface Game {
    grid: Array<Array<number>>;
    score: number;
    gameover: boolean;
    reset(): void;
    step(direction: number): number;
}

interface Direction {
    Up,
    Right,
    Down,
    Left,
}

export class Interface {
    private game: Game;
    private direction: Direction;

    constructor(game: Game, direction: Direction) {
        this.game = game;
        this.direction = direction;
    }

    private center_string(s: string, size: number): string {
        return s.padStart(s.length + Math.floor((size - s.length) / 2), " ").padEnd(size, " ");
    }

    private get_str_val(x, y, size = 7): string {
        return this.center_string(this.game.grid[x][y].toString(), size);
    }

    private pprint() {
        console.log("|-------|-------|-------|-------|");
        console.log(`|${this.get_str_val(0,0)}|${this.get_str_val(0,1)}|${this.get_str_val(0,2)}|${this.get_str_val(0,3)}|`);
        console.log("|-------|-------|-------|-------|");
        console.log(`|${this.get_str_val(1,0)}|${this.get_str_val(1,1)}|${this.get_str_val(1,2)}|${this.get_str_val(1,3)}|`);
        console.log("|-------|-------|-------|-------|");
        console.log(`|${this.get_str_val(2,0)}|${this.get_str_val(2,1)}|${this.get_str_val(2,2)}|${this.get_str_val(2,3)}|`);
        console.log("|-------|-------|-------|-------|");
        console.log(`|${this.get_str_val(3,0)}|${this.get_str_val(3,1)}|${this.get_str_val(3,2)}|${this.get_str_val(3,3)}|`);
        console.log("|-------|-------|-------|-------|");
        console.log(`Score: ${this.game.score}`);
    }
    
    private async get_input() {
        
        let input = await question("");
        while (!["w", "a", "s", "d"].includes(input)) {
            input = await question("");
        }

        switch (input) {
            case "w":
                return this.direction.Up;
                break;
            case "d":
                return this.direction.Right;
                break;
            case "s":
                return this.direction.Down;
                break;
            case "a":
                return this.direction.Left;
                break;
        }
    }

    private async move() {
        let direction = await this.get_input();
        let reward = this.game.step(direction);
        return reward;
    }

    private async handle_gameover(): Promise<boolean> {
        this.pprint();
        console.log("Game over!")
        let answer = await question("Restart? [Y/n]")
        if (["n", "no"].includes(answer.toLowerCase())) {
            return false
        }
        return true
    }

    async main() {
        this.game.reset();

        while (true) {
            this.pprint();
            await this.move();

            if (this.game.gameover) {
                if (!await this.handle_gameover()) {
                    break;
                }
                this.game.reset();
            }
        }
    }
}
