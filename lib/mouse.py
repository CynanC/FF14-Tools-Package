import time
import win32api,win32gui,win32con
from ctypes import *

def left():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
	time.sleep(0.02)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def right():
	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
	time.sleep(0.02)
	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

def left_down():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

def left_up():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def move(x,y):
    windll.user32.SetCursorPos(x, y)


if __name__=='__main__':
	move(1855,1010)
	time.sleep(0.02)
	left()
	# for i in range(10):
	# 	click_l()
	# 	time.sleep(0.1)