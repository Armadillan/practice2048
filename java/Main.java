import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        CMC grid = new CMC();
        Interface game = new Interface(grid);
        game.main();
    }
}
