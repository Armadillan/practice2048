import java.lang.Long;
import java.lang.String;
import java.util.Arrays;

import helpers.GameInterface;
import helpers.Direction;
import helpers.CenterString;
public class Interface {
    private GameInterface game;
    private static int padSize = 7;

    public Interface(GameInterface game) {
        this.game = game;
    }

    private String getStringVal(int x, int y, int size) {
        return CenterString.centerString(Long.toString(game.getGrid()[x][y]), size);
    }

    private String getRowString(int row, int pad_size) {
        String out = "|";
        for (int i = 0; i < 4; i++) {
            out = out + getStringVal(row, i, pad_size);
            out = out + "|";
        }
        return out;
    }

    private void pprint(int pad_size) {
        for (int i = 0; i < 4; i++) {
            System.out.println("|-------|-------|-------|-------|");
            System.out.println(getRowString(i, pad_size));
        }
        System.out.println("|-------|-------|-------|-------|");
        System.out.println(String.format("Score: %s", game.getScore()));
    }

    private Direction get_input() {
        String input = new String();
        while (!Arrays.asList("w", "a", "s", "d").contains(input)) {
            input = System.console().readLine();
        }
        switch (input) {
            case "w":
                return Direction.Up;
            case "d":
                return Direction.Right;
            case "s":
                return Direction.Down;
            default:
            case "a":
                return Direction.Left;
        }
    }

    private long move() {
        Direction direction = get_input();
        long reward = game.step(direction);
        return reward;
    }

    private boolean handle_gameover() {
        pprint(padSize);
        System.out.println("Game over!");
        System.out.println("Restart? [Y/n]");
        String answer = System.console().readLine();
        if (Arrays.asList("no", "n").contains(answer.toLowerCase())) {
            return false;
        }
        return true;
    }

    public void main() {
        game.reset();

        while (true) {
            pprint(padSize);
            move();

            if (game.gameover()) {
                if (handle_gameover()) {
                    break;
                }
                game.reset();
            }
        }
    }
}
