# practice2048
2048 in Python, Rust, C, C++, TypeScript (Node.js), Java and Go. Practicing programming languages.

Two different implementations:
* Everything At Once (EAO), where each move happens in one step, like in https://github.com/Armadillan/TensorFlow2048. Moving and merging each tile one at a time.
* Compress-Merge-Compress (CMC), where each move is made up of moving cells as far as they go, merging neighbours of the same value, and moving again. Now with rotation!

All implementations should:
* Be playable with a console frontnend
* Optionally with a GUI frontend
* Track score
* Stop the game on gameover and give the option to restart

### Progress:
| Language   | EAO | CMC | Frontend |
|------------|:---:|:---:|:--------:|
| Python     |  X  |  X  |     X    |
| TypeScript |  X  |  X  |     X    |
| Rust       |  X  |  X  |     X    |
| Java       |     |  X  |     X    |
| C++        |     |     |          |
| C          |     |     |          |
| Go         |     |     |          |

Next step could maybe be Electron GUI?

2048 was originally created by Gabriele Cirulli and can be found [here](https://play2048.co/).
