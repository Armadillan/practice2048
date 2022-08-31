import cmc
import eao
import gui
import console_frontend

# game = console_frontend.Interface(cmc.Game())
game = gui.Interface(eao.Game())

game.main()