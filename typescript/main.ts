import * as cmc  from "./cmc";
import { Interface } from "./console_frontend";

let game = new cmc.Game();

let frontend = new Interface(game, cmc.Direction);

frontend.main();
