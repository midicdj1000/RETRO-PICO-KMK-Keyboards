

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

#from kmk.modules.layers import Layers


print("Starting")
keyboard = KMKKeyboard()
#keyboard.debug_enabled = True
#keyboard.modules.append(Layers())
#zx+2a

keyboard.col_pins = (
board.GP27,
board.GP26,
board.GP22,
board.GP21,
board.GP20,
board.GP19,
board.GP18,
board.GP17,
board.GP16,
board.GP15,
board.GP14,
)
keyboard.row_pins = (
board.GP13,
board.GP12,
board.GP11,
board.GP10,
board.GP9,
board.GP8,
board.GP7,
board.GP6,
board.GP5,
board.GP4,
board.GP3,
board.GP2,
board.GP28,
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

#MOMENTARY = KC.MO(1)

keyboard.keymap = [
    [ KC.N1   ,KC.N2   ,KC.N3   ,KC.N4   ,KC.N5   ,KC.NO      ,KC.NO        ,KC.NO   ,KC.NO   ,KC.NO    ,KC.NO,
      KC.Q    ,KC.W    ,KC.E    ,KC.R    ,KC.T    ,KC.NO      ,KC.NO        ,KC.NO   ,KC.NO   ,KC.NO    ,KC.NO,
      KC.A    ,KC.S    ,KC.D    ,KC.F    ,KC.G    ,KC.NO      ,KC.NO        ,KC.NO   ,KC.NO   ,KC.NO    ,KC.NO,
      KC.N0   ,KC.N9   ,KC.N8   ,KC.N7   ,KC.N6   ,KC.NO      ,KC.NO        ,KC.NO   ,KC.NO   ,KC.NO    ,KC.NO,
      KC.P    ,KC.O    ,KC.I    ,KC.U    ,KC.Y    ,KC.NO      ,KC.NO        ,KC.NO   ,KC.NO   ,KC.NO    ,KC.NO,
      KC.CAPS ,KC.Z    ,KC.X    ,KC.C    ,KC.V    ,KC.NO      ,KC.NO        ,KC.NO   ,KC.NO   ,KC.NO    ,KC.NO,
      KC.ENT  ,KC.L    ,KC.K    ,KC.J    ,KC.H    ,KC.NO      ,KC.NO        ,KC.NO   ,KC.NO   ,KC.NO    ,KC.NO,
      # SPACE = 77
      KC.SPACE,KC.LSFT ,KC.M    ,KC.N    ,KC.B    ,KC.N1      ,KC.N2        ,KC.N3   ,KC.N4   ,KC.N5    ,KC.N6,
      KC.NO   ,KC.NO   ,KC.NO   ,KC.NO   ,KC.NO   ,KC.N1      ,KC.N2        ,KC.N3   ,KC.N4   ,KC.SCOLON    ,KC.DQUO,
      KC.NO   ,KC.NO   ,KC.NO   ,KC.NO   ,KC.NO   ,KC.DOT     ,KC.COMMA     ,KC.N3   ,KC.N4   ,KC.N5    ,KC.N6,
      KC.NO   ,KC.NO   ,KC.NO   ,KC.NO   ,KC.NO   ,KC.LBRACKET      ,KC.RBRACKET        ,KC.PERCENT   ,KC.CAPS   ,KC.LEFT    ,KC.N6,
      KC.NO   ,KC.NO   ,KC.NO   ,KC.NO   ,KC.NO   ,KC.RIGHT      ,KC.UP        ,KC.BSPC   ,KC.ASTERISK   ,KC.DOWN    ,KC.N6,
      KC.NO   ,KC.NO   ,KC.NO   ,KC.NO   ,KC.NO   ,KC.N1      ,KC.N2        ,KC.BRK   ,KC.EXCLAIM   ,KC.N5    ,KC.N6,
    ]

]

if __name__ == '__main__':
    keyboard.go()
