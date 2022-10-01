package helpers;

public interface GameInterface {
    public long[][] getGrid();
    public long getScore();
    public void reset();
    public long step(Direction direction);
    public boolean gameover();

}
