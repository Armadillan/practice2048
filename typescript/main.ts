import * as cmc  from "./cmc";
import * as eao from "./eao";
import { Interface } from "./console_frontend";

// let game = new cmc.Game();
let game = new eao.Game();

// let frontend = new Interface(game, cmc.Direction);
let frontend = new Interface(game, eao.Direction);

frontend.main();
