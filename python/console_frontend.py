from collections import defaultdict

class Interface:

    def __init__(self, game):
        self.game = game
        self.score = 0
        self.gameover = False

    def get_str_val(self, *coords):
        return str(self.game.state[coords[0], coords[1]]).center(7)

    def pprint(self):
        #this is actually a better way to do it than looping in my opinion
        #easier to change the code
        #would need refactor for different grid size
        print(f"""|-------|-------|-------|-------|
|{self.get_str_val(0,0)}|{self.get_str_val(0,1)}|{self.get_str_val(0,2)}|{self.get_str_val(0,3)}|
|-------|-------|-------|-------|
|{self.get_str_val(1,0)}|{self.get_str_val(1,1)}|{self.get_str_val(1,2)}|{self.get_str_val(1,3)}|
|-------|-------|-------|-------|
|{self.get_str_val(2,0)}|{self.get_str_val(2,1)}|{self.get_str_val(2,2)}|{self.get_str_val(2,3)}|
|-------|-------|-------|-------|
|{self.get_str_val(3,0)}|{self.get_str_val(3,1)}|{self.get_str_val(3,2)}|{self.get_str_val(3,3)}|
|-------|-------|-------|-------|""")
        print(f"Score: {self.score}")

    input_dict = {
        "w": 0,
        "d": 1,
        "s": 2,
        "a": 3,
    }
    def get_input(self):
        #should block until arrow keys or wasd pressed
        #temp solution using input()
        #work on finding cross-platform solution not requiring pressing enter
        direction = None
        while direction is None:
            direction = self.input_dict.get(input())
        return direction

    def move(self, direction):
        _, reward = self.game.step(direction)
        self.score += reward

    def handle_gameover(self) -> bool:
        # True if continue, False if end game.
        self.pprint()
        print("Game over!")
        if input("Exit? [N/y]").lower() in ("y", "yes"):
            return False
        return True

    def main(self):

        self.game.reset()

        while True:
            self.pprint()
            self.move(self.get_input())

            if self.game.gameover:
                if self.handle_gameover():
                    self.game.reset()
                else:
                    break

if __name__ == "__main__":
    import cmc
    Game = Interface(cmc.Game())
    Game.main()