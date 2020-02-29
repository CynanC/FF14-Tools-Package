import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)

KEYCODE={"D": 0x20, "F6": 0x40, "Ctrl F3": 0x60, "Alt 9": 0x80, "Alt Dn Arrow": 0xA0, 
"ESC": 0x01, "F": 0x21, "F7": 0x41, "Ctrl F4": 0x61, "Alt 0": 0x81, "Alt PgDn": 0xA1, 
"1": 0x02, "G": 0x22, "F8": 0x42, "Ctrl F5": 0x62, "Alt - ": 0x82, "Alt Ins": 0xA2, 
"2": 0x03, "H": 0x23, "F9": 0x43, "Ctrl F6": 0x63, "Alt =": 0x82, "Alt Del": 0xA3, 
"3": 0x04, "J": 0x24, "F10": 0x44, "Ctrl F7": 0x64, "Ctrl PgUp": 0x84, "Alt / (num)": 0xA4, 
"4": 0x05, "K": 0x25, "Num Lk": 0x45, "Ctrl F8": 0x65, "F11": 0x85, "Alt Tab": 0xA5, 
"5": 0x06, "L": 0x26, "Scrl Lk": 0x46, "Ctrl F9": 0x66, "F12": 0x86, "Alt Enter (num)": 0xA6, 
"6": 0x07, "; : ": 0x27, "Home": 0x47, "Ctrl F10": 0x67, "SH F11": 0x87, 
"7": 0x08, "' \"": 0x28, "Up Arrow": 0x48, "Alt F1": 0x68, "SH F12": 0x88, 
"8": 0x09, "` ~": 0x29, "Pg Up": 0x49, "Alt F2": 0x69, "Ctrl F11": 0x89, 
"9": 0x0A, "L SH": 0x2A, "- (num)": 0x4A, "Alt F3": 0x6A, "Ctrl F12": 0x8A, 
"0": 0x0B, "\ |": 0x2B, "4 Left Arrow": 0x4B, "Alt F4": 0x6B, "Alt F11": 0x8B, 
"- _": 0x0C, "Z": 0x2C, "5 (num) ": 0x4C, "Alt F5": 0x6C, "Alt F12": 0x8C, 
"= +": 0x0D, "X": 0x2D, "6 Rt Arrow": 0x4D, "Alt F6": 0x6D, "Ctrl Up Arrow": 0x8C, 
"BKSP": 0x0E, "C": 0x2E, "+ (num)": 0x4E, "Alt F7": 0x6E, "Ctrl - (num)": 0x8E, 
"Tab": 0x0F, "V": 0x2F, "1 End": 0x4F, "Alt F8": 0x6F, "Ctrl 5 (num)": 0x8F, 
"Q": 0x10, "B": 0x30, "2 Dn Arrow": 0x50, "Alt F9": 0x70, "Ctrl + (num)": 0x90, 
"W": 0x11, "N": 0x31, "3 Pg Dn": 0x51, "Alt F10": 0x71, "Ctrl Dn  Arrow": 0x91, 
"E": 0x12, "M": 0x32, "0 Ins": 0x52, "Ctrl PtScr": 0x72, "Ctrl Ins": 0x92, 
"R": 0x13, ",  <": 0x33, "Del .": 0x53, "Ctrl L Arrow": 0x73, "Ctrl Del": 0x93, 
"T": 0x14, ". >": 0x34, "SH F1": 0x54, "Ctrl R Arrow": 0x74, "Ctrl Tab": 0x94, 
"Y": 0x15, "/ ?": 0x35, "SH F2": 0x55, "Ctrl End": 0x75, "Ctrl / (num)": 0x95, 
"U": 0x16, "R SH": 0x36, "SH F3": 0x56, "Ctrl PgDn": 0x76, "Ctrl * (num)": 0x96, 
"I": 0x17, "PtScr": 0x37, "SH F4": 0x57, "Ctrl Home": 0x77, "Alt Home": 0x97, 
"O": 0x18, "Alt": 0x38, "SH F5": 0x58, "Alt 1": 0x78, "Alt Up Arrow": 0x98, 
"P": 0x19, "Spc": 0x39, "SH F6": 0x59, "Alt 2": 0x79, "Alt PgUp": 0x99, 
"[ {": 0x1A, "CpsLk": 0x3A, "SH F7": 0x5A, "Alt 3": 0x7A,
"] }": 0x1B, "F1": 0x3B, "SH F8": 0x5B, "Alt 4": 0x7B, "Alt Left Arrow": 0x9B, 
"Enter": 0x1C, "F2": 0x3C, "SH F9": 0x5C, "Alt 5": 0x7C, "`":0x29,
"Ctrl": 0x1D, "F3": 0x3D, "SH F10": 0x5D, "Alt 6": 0x7D, "Alt Rt Arrow": 0x9D, 
"A": 0x1E, "F4": 0x3E, "Ctrl F1": 0x5E, "Alt 7": 0x7E, "Shift":0x2A,
"S": 0x1F, "F5": 0x3F, "Ctrl F2": 0x5F, "Alt 8": 0x7F, "Alt End": 0x9F}


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def press(key):
	PressKey(KEYCODE[key])
def release(key):
	ReleaseKey(KEYCODE[key])

if __name__=='__main__':
	for i in range(5):
	    press('1')
	    time.sleep(0.5)
	    release('1')
	    time.sleep(0.5)