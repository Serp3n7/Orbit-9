import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_ssd1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.handlers.sequences import send_string
from kmk.extensions.pegasus_oled_ssd1306 import PegasusOLED

keyboard = KMKKeyboard()

# --- 1. HARDWARE PINOUT ---
keyboard.col_pins = (board.D2, board.D3, board.D6)
keyboard.row_pins = (board.D7, board.D8, board.D9, board.D10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# --- 2. ENCODER SETUP ---
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.D0, board.D1, None, False),)

# --- 3. OLED UI SETUP ---
i2c_bus = busio.I2C(board.D5, board.D4) 

class OrbitOLED(PegasusOLED):
    def render(self):
        layer = keyboard.active_layers[0]
        if layer == 0:
            text = "NAVIGATE\n--------\nVol Ctrl"
        elif layer == 1:
            text = "MEDIA\n--------\nBrightns"
        elif layer == 2:
            text = "DESIGN\n--------\nZoom/Scr"
        else:
            text = "Orbit-9"
        self.set_text(text, 0, 0)

oled_ext = OrbitOLED(i2c_bus)
keyboard.extensions.append(oled_ext)

# --- 4. MODULES & MACROS ---
layers = Layers()
keyboard.modules.append(layers)
keyboard.extensions.append(MediaKeys())

def code_format(): keyboard.tap_key(KC.LSFT(KC.LALT(KC.F)))

# Layer Shifters
TO_BASE = KC.TO(0)
TO_MEDIA = KC.TO(1)
TO_DESIGN = KC.TO(2)

# --- 5. KEYMAPS ---

# LAYER 0: WINDOW NAVIGATOR (Productivity Base)
# Knob: Volume (Always useful)
L0_MAP = [
    # Row 1: Virtual Desktops & Task View
    [ KC.LCTL(KC.LGUI(KC.LEFT)), KC.LGUI(KC.TAB),     KC.LCTL(KC.LGUI(KC.RIGHT)) ], 
    # (Desktop Left),            (Task View),         (Desktop Right)

    # Row 2: Window Snapping (Split Screen)
    [ KC.LGUI(KC.LEFT),          KC.LGUI(KC.UP),      KC.LGUI(KC.RIGHT)          ],
    # (Snap Left),               (Maximize),          (Snap Right)

    # Row 3: App Switching & Minimizing
    [ KC.LALT(KC.TAB),           KC.LGUI(KC.DOWN),    KC.LGUI(KC.LSFT(KC.S))     ],
    # (Alt-Tab),                 (Minimize/Restore),  (Screenshot Tool)

    # Row 4: Encoder Switch -> Go to Media
    [ TO_MEDIA,                  KC.NO,               KC.NO                      ]  
]
L0_ENC = ( (KC.VOLU, KC.VOLD, None), ) 

# LAYER 1: MEDIA
L1_MAP = [
    [ KC.MPRV, KC.MPLY, KC.MNXT ],
    [ KC.MUTE, KC.VOLD, KC.VOLU ],
    [ KC.NO,   KC.NO,   KC.NO   ],
    [ TO_DESIGN, KC.NO, KC.NO   ]  # Switch click -> Go to Design Layer
]
L1_ENC = ( (KC.BRIU, KC.BRID, None), )

# LAYER 2: DESIGN (Fusion 360 / VS Code)
L2_MAP = [
    [ KC.LCTL(KC.Z),  KC.LCTL(KC.C),   KC.LCTL(KC.V)       ], # Undo, Copy, Paste
    [ KC.LCTL(KC.B),  KC.LCTL(KC.S),   KC.LCTL(KC.LSFT(KC.P)) ], # Sidebar, Save, Cmd Palette
    [ KC.F6,          KC.LSFT(KC.LALT(KC.F)), KC.LALT(KC.TAB) ], # Fit View, Format, Alt-Tab
    [ TO_BASE,        KC.NO,           KC.NO               ] # Back to Navigator
]
L2_ENC = ( (KC.LCTL(KC.MW_UP), KC.LCTL(KC.MW_DN), None), )

# --- APPLY ---
keyboard.keymap = [
    [key for row in L0_MAP for key in row],
    [key for row in L1_MAP for key in row],
    [key for row in L2_MAP for key in row]
]
encoder_handler.map = [L0_ENC, L1_ENC, L2_ENC]

if __name__ == '__main__':
    keyboard.go()