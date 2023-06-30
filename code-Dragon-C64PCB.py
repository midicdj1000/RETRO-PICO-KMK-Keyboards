# Dragon 32/64 Keyboard to USB Keyboard suitable for XRoar with translate OFF
#	Wayland, Robcfg
#
# Uses KMK Librarys for PI Pico.
# Uses Lee Smith's C64 PCB layout https://github.com/midicdj1000/RETRO-PICO-KMK-Keyboards
#
# The symbol keys do not actually return what's printed on them except in XRoar 
# which knows what they are supposed to do on the Dragon.
# 2023/04/15 Mostly working. Problems with some symbols, £ @ * =
# 2023/04/16 Works with XRoar. Everything except @ which comes out as "
# 2023/04/18 Finished for XRoar. All keys working.
# 2023/06/29 Modified config so that it works with all keyboards and doesn't need
#            to modify XRoar's config to get the @ symbol.

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers


print("Starting")
keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
#C64 pcb
keyboard.debug_enabled = True
keyboard.col_pins = (
 board.GP8 ,#9
 board.GP9 ,#10
 board.GP10,#11
 board.GP11,#13
 board.GP12,#12
 board.GP13,#14
 board.GP14,#15
 board.GP15,#16
)
keyboard.row_pins = (
  board.GP26,#1
  board.GP22,#2
  # Note: Pin #3 is not assigned as it's the GND pin
  board.GP20,#4
  board.GP16,#5
  board.GP17,#6
  board.GP18,#7
  board.GP19,#8
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

#   Dragon 32/64 Matrix from Dragon schematic
#
#          LSB              $FF02                    MSB
#        | PB0   PB1   PB2   PB3   PB4   PB5   PB6   PB7 <- column
#    ----|----------------------------------------------
#    PA0 |   0     1     2     3     4     5     6     7    LSB
#    PA1 |   8     9     :     ;     ,     -     .     /     $
#    PA2 |   @     A     B     C     D     E     F     G     F
#    PA3 |   H     I     J     K     L     M     N     O     F
#    PA4 |   P     Q     R     S     T     U     V     W     0
#    PA5 |   X     Y     Z    Up  Down  Left Right Space     0
#    PA6 | ENT   CLR   BRK   N/C   N/C   N/C   N/C  SHFT
#     ^
#     |
#    row

# PC keymap
#keyboard.keymap = [
#    [ KC.N0,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7, 
#      KC.N8,  KC.N9,   KC.COLN, KC.SCLN, KC.COMM, KC.MINS, KC.DOT,  KC.SLSH, 
#      KC.AT,  KC.A,    KC.B,    KC.C,    KC.D,    KC.E,    KC.F,    KC.G, 
#      KC.H,   KC.I,    KC.J,    KC.K,    KC.L,    KC.M,    KC.N,    KC.O, 
#      KC.P,   KC.Q,    KC.R,    KC.S,    KC.T,    KC.U,    KC.V,    KC.W, 
#      KC.X,   KC.Y,    KC.Z,    KC.UP,   KC.DOWN, KC.LEFT ,KC.RIGHT,KC.SPC, 
#      KC.ENT, KC.HOME, KC.ESC,  KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.LSFT
#    ]
#]

# XRoar keymap
keyboard.keymap = [
    [ KC.N0,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7, 
      KC.N8,  KC.N9,   KC.MINS, KC.SCLN, KC.COMM, KC.EQL,  KC.DOT,  KC.SLSH, 
      KC.LBRC,KC.A,    KC.B,    KC.C,    KC.D,    KC.E,    KC.F,    KC.G, 
      KC.H,   KC.I,    KC.J,    KC.K,    KC.L,    KC.M,    KC.N,    KC.O, 
      KC.P,   KC.Q,    KC.R,    KC.S,    KC.T,    KC.U,    KC.V,    KC.W, 
      KC.X,   KC.Y,    KC.Z,    KC.UP,   KC.DOWN, KC.LEFT, KC.RIGHT,KC.SPC, 
      KC.ENT, KC.HOME, KC.ESC,  KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.LSFT
    ]
]

if __name__ == '__main__':
    keyboard.go()
