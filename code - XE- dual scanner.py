
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import KeysScanner
from kmk.scanners.digitalio import MatrixScanner
#Atari XE
print("Starting")

_KEY_CFG = [
    board.GP2,  board.GP3,  board.GP4, board.GP5,
]

coord_mapping = [
    0, 1, 2, 3, 4, 5, 6, 7, 8,
    9, 10, 11, 12, 13, 14, 15, 16,
    17, 18, 19, 20, 21, 22, 23, 24,
    25, 26, 27, 28, 29, 30, 31, 32,
    33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48,
    49, 50, 51, 52, 53, 54, 56, 56,
    57, 58, 59, 60, 61, 62, 63, 64,
    65, 66, 67, 68,
 ]

_COL_PINS = (
 board.GP6,#9
 board.GP7,#10
 board.GP22,#11
 board.GP17,#13
  board.GP18,#12
 board.GP19, #14
 board.GP8,#15
 board.GP14,#16
 board.GP13,#17
 #board.GP26,#
)

_ROW_PINS = (
  board.GP10, #1
  board.GP11,#2
  board.GP9, #3
  board.GP12,#4
  board.GP16,#5
  board.GP15, #6
  board.GP21, #7
  board.GP20,#8
   #board.GP2,#8
   #board.GP3,#8
  #board.GP4,#8
  #board.GP5,#8
)

# Keyboard implementation class
class MyKeyboard(KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = [
            MatrixScanner(
                # required arguments:
                cols=_COL_PINS,
                rows=_ROW_PINS,
                # optional arguments with defaults:
                diode_orientation = DiodeOrientation.COLUMNS,
                #interval=0.02,
                #max_events=64
            ),
            KeysScanner(
                # require argument:
                pins=_KEY_CFG,
                # optional arguments with defaults:
                value_when_pressed=False,
                pull=True,
                interval=0.02,
                max_events=64
            ),
        ]



keyboard = MyKeyboard()
#keyboard.debug_enabled = True



keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.keymap = [
    [
    KC.GRV,KC.N7,KC.NO,KC.N8,KC.N9,KC.N0,KC.MINS,KC.EQL,KC.BSPC,#1
    KC.NO,KC.N6,KC.NO,KC.N5,KC.N4,KC.N3,KC.N2,KC.N1,KC.ESC,#2
    KC.NO,KC.U,KC.NO,KC.I,KC.O,KC.P,KC.LBRC,KC.RBRC,KC.ENT,#3
    KC.NO,KC.Y,KC.NO,KC.T,KC.R,KC.E,KC.W,KC.Q,KC.TAB,#4
    KC.LCTL,KC.NO,KC.J,KC.K,KC.L,KC.SCLN,KC.QUOTE,KC.BSLS,KC.NO,#5
    KC.NO,KC.NO,KC.H,KC.G,KC.F,KC.D,KC.S,KC.A,KC.CAPS,KC.N4,#6
    KC.NO,KC.N,KC.SPACE,KC.M,KC.COMM,KC.DOT,KC.SLSH,KC.RALT,KC.NO,#7
    KC.LSFT,KC.NO,KC.HOME,KC.B,KC.V,KC.C,KC.X,KC.Z,#8
    KC.N1, KC.N2, KC.N3, KC.N4,
    ]
]






if __name__ == '__main__':
    keyboard.go()

