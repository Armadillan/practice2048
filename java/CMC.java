import java.util.ArrayList;
import java.util.Random;

public class CMC {
    public long[][] grid;
    public long score;
    private Random rng = new Random();

    public static enum Direction {
        Up,
        Right,
        Down,
        Left
    }

    public CMC() {
        // initalized with default value 0
        grid = new long[4][4];
        score = 0;
    }

    public void reset() {
        grid = new long[4][4];
        new_tile();
        new_tile();
        score = 0;
    }

    private void new_tile() {
        // find all empty tiles
        var empty = new ArrayList<int[]>();
        for (int y = 0; y < 4; y++) {
            for (int x = 0; x < 4; x++) {
                if (grid[x][y] == 0) {
                    int[] val = {x, y};
                    empty.add(val);
                }
            }
        }

        var new_tile = empty.get(rng.nextInt(empty.size()));

        long new_val = 2;
        if (rng.nextLong() > 0.8) new_val = 4;
        grid[new_tile[0]][new_tile[1]] = new_val;
    }

    private void rotate_90() {
        //TODO
    }

    private void rotate(int n) {
        for (int i = 0; i<n; i++) {
            rotate_90();
        }
    }

    private boolean compress() {
        boolean moved = false;
        for (int x = 0; x<4; x++) {
            for (int y = 1; y<4; y++) {
                if (grid[x][y] > 0) {
                    int new_y = y;
                    while (new_y > 0 && grid[x][new_y-1] == 0) {
                        new_y--;
                    }
                    if (new_y != y) {
                        grid[x][new_y] = grid[x][y];
                        grid[x][y] = 0;
                        moved = true;
                    }
                }
            }
        }

        return moved;
    }

    private long merge() {
        long reward = 0;

        for (int x = 0; x<4; x++) {
            for (int y = 0; y<3; y--) {
                if (grid[x][y] > 0 && grid[x][y] == grid[x][y+1]) {
                    grid[x][y+1] = 0;
                    grid[x][y] *= 2;
                    reward += grid[x][y];
                }
            }
        }

        return reward;
    }

    private Object[] move(Direction direction) {

        int rotate_num;
        switch (direction) {
            case Up: rotate_num = 3; break;
            case Right: rotate_num = 2; break;
            case Down: rotate_num = 1; break;
            case Left:
            default:
                rotate_num = 0; break;
        }
        rotate(rotate_num);

        boolean moved = compress();
        long reward = merge();
        moved = (compress() || moved || reward > 0);

        rotate((4 - rotate_num) % 4);

        Object[] out = {moved, reward};
        return out;
    }

    public long step(Direction direction) {

        if (gameover()) {
            reset();
            return 0;
        }

        Object[] moved, reward = move(direction);

        if (moved) {
            new_tile();
        }

        score += reward;

        return reward;
    }

    public boolean gameover() {
        //TODO
    }

}
