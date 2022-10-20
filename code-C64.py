

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.modules.layers import Layers


print("Starting")
keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
#c64
#keyboard.debug_enabled = True
keyboard.row_pins = (
 board.GP8,#9
 board.GP9,#10
 board.GP10,#11
 board.GP11,#13
  board.GP12,#12
 board.GP13, #14
 board.GP14,#15
 board.GP15,#16
)
keyboard.col_pins = (
  board.GP26, #1
  board.GP22,#2
  board.GP21, #3
  board.GP20,#4
  board.GP16,#5
  board.GP17, #6
  board.GP18, #7
  board.GP19,#8
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

MOMENTARY = KC.MO(1)

keyboard.keymap = [
    [KC.N1,KC.N3,KC.N5,KC.N7,KC.N9,KC.PLUS,KC.BSLS,KC.DEL,
    KC.GRV,KC.W,KC.R,KC.Y,KC.I,KC.P,KC.ASTR,KC.ENTER,
    KC.LCTL,KC.A,KC.D,KC.G,KC.J,KC.L,KC.QUOT,KC.LEFT,
    KC.ESC,KC.LSFT,KC.X,KC.V,KC.N,KC.COMM,KC.SLSH,KC.UP,
    KC.SPC,KC.Z,KC.C,KC.B,KC.M,KC.DOT,MOMENTARY,KC.F1,
    KC.TAB,KC.S,KC.F,KC.H,KC.K,KC.SCLN,KC.F10,KC.F3,
    KC.Q,KC.E,KC.T,KC.U,KC.O,KC.LBRC,KC.F9,KC.F5,
    KC.N2,KC.N4,KC.N6,KC.N8,KC.N0,KC.MINS,KC.HOME,KC.F7,
    ],
     [KC.N1,KC.N3,KC.N5,KC.N7,KC.N9,KC.PLUS,KC.BSLS,KC.DEL,
    KC.GRV,KC.W,KC.R,KC.Y,KC.I,KC.P,KC.ASTR,KC.ENTER,
    KC.LCTL,KC.A,KC.D,KC.G,KC.J,KC.L,KC.QUOT,KC.RIGHT,
    KC.ESC,KC.LSFT,KC.X,KC.V,KC.N,KC.COMM,KC.SLSH,KC.DOWN,
    KC.SPC,KC.Z,KC.C,KC.B,KC.M,KC.DOT,KC.TRNS,KC.F2,
    KC.TAB,KC.S,KC.F,KC.H,KC.K,KC.SCLN,KC.F10,KC.F4,
    KC.Q,KC.E,KC.T,KC.U,KC.O,KC.LBRC,KC.F9,KC.F6,
    KC.N2,KC.N4,KC.N6,KC.N8,KC.N0,KC.MINS,KC.HOME,KC.F8,
    ]
]

if __name__ == '__main__':
    keyboard.go()
