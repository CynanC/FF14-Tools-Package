# from PIL import Image
# from PIL import ImageFilter
import numpy as np
# import matplotlib.pyplot as plt
from lib.catch import *
import lib.mouse as mouse
from lib.listen_key import *
from lib.play_mp3 import play_mp3
from threading import Thread
import os


CROP=[698,925,1138,943]

def locate_img_array(crop):
	LINE=5
	array_im=get_screen_arry(crop)
	for x in range(len(array_im))[::-1]:
		if array_im[x][LINE][0]>200 and array_im[x][LINE][1]>200:
			return x
	return 0


def start_boxing():
	error_num=0
	while 1:
		if IF_START==0:break
		if error_num>=10:break
		mouse.move(966,370)
		mouse.left()
		time.sleep(0.05)
		mouse.right()
		time.sleep(1)
		mouse.move(970,580)
		mouse.left()
		time.sleep(0.05)
		mouse.move(1230,915)
		loc=0
		loc_p=0
		try:
			start_time=time.time()
			while 1:
				if IF_START==0:break
				if time.time()-start_time>15: break
				loc=locate_img_array(CROP)
				if loc in range(135,151) and loc_p<loc and loc_p!=0:
					print("Right:\t"+str(loc))
					mouse.left()
					break
				if loc in range(280,301) and loc_p>loc and loc_p!=0:
					print("Left:\t"+str(loc))
					mouse.left()
					break
				loc_p=loc
			time.sleep(5)
		except Exception as e:
			print('Got an error:', e)
			error_num+=1

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        relative_path='lib/'+relative_path
    return os.path.join(base_path, relative_path)

def on_press(key):
	global IF_START
	try:
		if key._name_=='f12':
			return False
		
		if key._name_=='caps_lock' and IF_START==0:
			play_mp3(resource_path('start.mp3'))
			print('START CUTTING')
			IF_START=1
			Thread(target=start_boxing).start()
		elif key._name_=='caps_lock':
			play_mp3(resource_path('end.mp3'))
			print('END CUTTING')
			IF_START=0
	except:
		pass

print('Press Caps to Start...')
IF_START=0
start_listen(on_press)