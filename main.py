from tablero import Tablero
from tablero_consola import Tablero_Consola



# tbl = Tablero_Consola(20,7)
# tbl.draw_board()

tbl2 = Tablero(20,7)
tbl2.initialize_pygame()
tbl2.draw_board()