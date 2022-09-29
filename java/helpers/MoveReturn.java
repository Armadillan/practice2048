package helpers;

//dataclass for returns from move function
public class MoveReturn {
    private final boolean moved;
    private final long reward;

    public MoveReturn(boolean moved, long reward) {
        this.moved = moved;
        this.reward = reward;
    }

    public boolean moved() {
        return moved;
    }

    public long reward() {
        return reward;
    }
}
