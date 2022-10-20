

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

#from kmk.modules.layers import Layers


print("Starting")
keyboard = KMKKeyboard()
#keyboard.debug_enabled = True
#keyboard.modules.append(Layers())
#cpc464

keyboard.col_pins = (
#board.GP27,
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
#board.GP3,
#board.GP2,
#board.GP28,
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

#MOMENTARY = KC.MO(1)

keyboard.keymap = [
    [ KC.BSPC ,KC.NO ,KC.NO ,KC.NO ,KC.NO ,KC.NO ,KC.NO ,KC.NO ,KC.NO ,KC.NO,KC.NO,
      KC.N1 ,KC.N2 ,KC.ESC ,KC.Q ,KC.TAB ,KC.A ,KC.CAPS ,KC.NO ,KC.Z ,KC.NO,
      KC.N4 ,KC.N3 ,KC.E ,KC.W ,KC.S ,KC.D ,KC.C ,KC.NO ,KC.X ,KC.NO,
      KC.N6 ,KC.N5 ,KC.R ,KC.T ,KC.G ,KC.F ,KC.B ,KC.NO ,KC.V ,KC.NO,
      KC.N8 ,KC.N7 ,KC.U ,KC.Y ,KC.H ,KC.J ,KC.N ,KC.NO ,KC.SPACE ,KC.NO,
      KC.N0 ,KC.N9 ,KC.O ,KC.I ,KC.L ,KC.K ,KC.M ,KC.NO ,KC.COMMA ,KC.NO,
      KC.EQL,KC.MINS ,KC.LBRC ,KC.P ,KC.QUOTE ,KC.SCLN ,KC.SLSH ,KC.NO ,KC.DOT ,KC.NO,
      KC.NO ,KC.RBRC ,KC.ENT ,KC.BSLS ,KC.P4 ,KC.LSFT ,KC.RSFT ,KC.NO,KC.LCTL,KC.NO,
      KC.LEFT ,KC.END ,KC.P7 ,KC.P8 ,KC.P5 ,KC.P1 ,KC.P2 ,KC.NO ,KC.P0 ,KC.NO,
      KC.UP ,KC.RIGHT ,KC.DOWN ,KC.P9 ,KC.P6 ,KC.P3 ,KC.PENT ,KC.NO ,KC.PDOT ,KC.NO ,
    ]

]

if __name__ == '__main__':
    keyboard.go()

