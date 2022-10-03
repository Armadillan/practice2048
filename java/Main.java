import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        // CMC grid = new CMC();
        EAO grid = new EAO();
        Interface game = new Interface(grid);
        game.main();
    }
}
