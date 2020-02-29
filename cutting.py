# -*- coding: utf-8 -*-  

import numpy as np
import math
import time
import lib.mouse as mouse
# import lib.key as key
from lib.catch import *
# from tkinter import *
from lib.listen_key import *
from lib.play_mp3 import play_mp3
from threading import Thread
import os

def transpose(array):
	array_T=np.zeros((len(array[0]),len(array))).tolist()	
	for i in range(0,len(array)):
		for j in range(0,len(array[0])):
			array_T[j][i]=array[i][j]
	return array_T


def blue_pos(a_im):
	pos=[0]*2
	for y in range(START_POINT[1],END_Y+1):
		x=pow(pow(START_POINT[0]-CENTER[0],2)+pow(START_POINT[1]-CENTER[1],2)-pow(y-CENTER[1],2),0.5)+CENTER[0]
		x=round(x)
		x=x-CROP[0]
		y=y-CROP[1]
		if a_im[x][y][0]<100 and a_im[x][y][1]<100 and a_im[x][y][2]>100:
			pos[0]=x+CROP[0]
			pos[1]=y+CROP[1]
			return pos
		# print(str(x+CROP[0])+','+str(y++CROP[1])+' '+str(a_im[y][x]))
	return pos

def white_pos(a_im):
	pos=[0]*2
	for y in range(START_POINT[1],END_Y+1):
		x=pow(pow(START_POINT[0]-CENTER[0],2)+pow(START_POINT[1]-CENTER[1],2)-pow(y-CENTER[1],2),0.5)+CENTER[0]
		x=round(x)
		x=x-CROP[0]
		y=y-CROP[1]
		if a_im[x][y][0]>150 and a_im[x][y][1]>150 and a_im[x][y][2]>150:
			pos[0]=x+CROP[0]
			pos[1]=y+CROP[1]
			return pos
	return pos
	# print(str(x)+','+str(y)+' '+str(a_im[y][x]))	


def radian(c,o1,o2):
	arc=pow(pow(o1[0]-o2[0],2)+pow(o1[1]-o2[1],2),0.5)/pow(pow(o1[0]-c[0],2)+pow(o1[1],c[1],2),0.5)/2
	if arc>1:arc=1
	if arc<-1:arc=-1
	return math.degrees(math.asin(arc))

def pos_r(pos):
	if pos[0]==0 and pos[1]==0:
		return 0
	return radian(CENTER,START_POINT,pos)

def find_white(a_im):
	#loction(490,403,515,803)
	LINE=10
	for i in range(len(a_im)):
		if int(a_im[i][LINE][0])+int(a_im[i][LINE][1])+int(a_im[i][LINE][2])>480:
			return i
	return 0

def find_red(a_im):
	#loction(490,403,515,803)
	LINE=8#8
	red_line=[]
	for i in range(len(a_im)):
		# if a_im[i][LINE][1]<80:
		if a_im[i][LINE][0]>100 and a_im[i][LINE][2]<80 and a_im[i][LINE][1]>80:
			red_line.append(i)
	return [red_line[0],red_line[-1]]

def find_pos(old=[]):
	new=[45,22.5,67.5,33.75,56.5,11.25,78.75]
	# num=len(old)
	# if old:
	# 	step=old[0]/2
	# 	for i in old:
	# 		new.append(i-step)
	# 		new.append(i+step)
	# else:
	# 	new.append(TOTAL_DEGREE/2)
	return new


def find_green(a_im):
	LINE=0
	for i in range(len(a_im)):
		if a_im[i][LINE][1]<100:
			return i/(len(a_im)-1)
	return 1

def axe(i,dely,bias):
	DELY2=0.25#0.2
	rp=0
	while 1:
		if IF_START==0:break
		if time.time()-START>65:break
		r=pos_r(white_pos(get_screen_arry(CROP)))
		if  i>=TOTAL_DEGREE/2 and r>=i-dely-bias  and r<=i-dely+bias and r>rp:
			print('Down:\t'+str(r))
			mouse.left()
			return [r,1]
		if i<=TOTAL_DEGREE/2 and r>=i+dely*DELY2-bias and r<=i+dely*DELY2+bias and r<rp:
			print('Up:\t'+str(r))
			mouse.left()
			return [r,2]
		rp=r

def start_cutting():
	global IF_START
	global START_POINT
	global CENTER
	global END_Y
	global TOTAL_DEGREE
	global CROP
	global START

	while 1:
		if IF_START==0:break

		mouse.move(965,380)
		mouse.left()
		time.sleep(0.05)
		mouse.right()
		time.sleep(1)


		CROP0=[427,472,452,872]

		try:
			red_line=find_red(transpose(get_screen_arry(CROP0)))
		except:
			continue
		if IF_START==0:break
		mouse.move(970,580)
		mouse.left()
		time.sleep(0.05)
		mouse.move(440,910)
		time.sleep(2)

		wp=0
		print(red_line)


		# dis_list=[]
		# for i in range(20):
		# 	if IF_START==0:break
		# 	dis=find_white(transpose(get_screen_arry(CROP0)))
		# 	dis=abs(find_white(transpose(get_screen_arry(CROP0)))-dis)
		# 	dis_list.append(dis)
		# dis=np.argmax(np.bincount(dis_list))

		dis=13
		dely=int(round(dis*4.75))
		bias=6
		START=time.time()
		while 1:
			if IF_START==0:break		
			if time.time()-START>10:break
			white_line=find_white(transpose(get_screen_arry(CROP0)))
			if red_line[0]>=200:
				if white_line in range(red_line[0]+bias-dely,red_line[1]-bias-dely+1) and white_line>wp:
					print('Down:\t'+str(white_line))
					mouse.left()
					break
			if red_line[0]<200:
				if white_line in range(red_line[0]+bias+dely,red_line[1]-bias+dely+1) and white_line<wp:
					print('Up:\t'+str(white_line))
					mouse.left()
					break
			wp=white_line
		if time.time()-START>10:
			mouse.move(1010,625)
			mouse.left()
			time.sleep(1.6)
			continue





		if IF_START==0:break
		CROP=[520,520,605,825]
		CENTER=[396,676]
		START_POINT=[536,532]
		END_Y=813
		END_X=round(pow(pow(START_POINT[0]-CENTER[0],2)+pow(START_POINT[1]-CENTER[1],2)-pow(END_Y-CENTER[1],2),0.5)+CENTER[0])
		TOTAL_DEGREE=pos_r([END_X,END_Y])
		CROP1=[332,854,656,855]
		time.sleep(3)
		START=time.time()
		dis_list=[]
		
		# for i in range (10):
		# 	if IF_START==0:break
		# 	dis=pos_r(white_pos(get_screen_arry(CROP)))
		# 	dis=abs(pos_r(white_pos(get_screen_arry(CROP)))-dis)
		# 	if dis!=0:dis_list.append(dis)
		# dis=np.median(dis_list)
		dis=6.2
		print('Speed:\t'+str(dis))
		dely=5*dis #4.5
		bias=3#3
		MOVE_AEX=10

		rounds=0
		while 1:

			if IF_START==0:break
			mouse.move(480,890)

			find_list=[]
			old_green=1

			while 1:
				if IF_START==0:break
				if time.time()-START>65:break
				find_list=find_pos(find_list)
				for i in find_list:
					if IF_START==0:break
					print('Find Pos:\t'+str(i))
					r=axe(i,dely,bias)
					time.sleep(3)
					green=find_green(get_screen_arry(CROP1))
					if green<1:break
				if green<1:break
			print('Green:\t'+str(green))
			
			ni=i
			move_aex=MOVE_AEX
			count_n=0
			while 1:
				skip_pos=0
				if IF_START==0:break
				if time.time()-START>65:break
				if green<0.05:break
				if old_green-green<=0.15:

					if ni==i-move_aex and old_green-green>=0.05 and count_n>=2:
						i=i-move_aex/2
						ni=i
						skip_pos=1
						count_n=0
					if ni==i+move_aex and old_green-green>=0.05 and count_n>=2:
						i=i+move_aex/2
						ni=i
						skip_pos=1
						count_n=0

					if i>=45 and not skip_pos:
						if ni<=i:
							ni=i+move_aex
							count_n+=1
						elif ni>=i:
							ni=i-move_aex
							count_n+=1
					if i<45 and not skip_pos:
						if ni>=i:
							ni=i-move_aex
							count_n+=1
						elif ni<=i:
							ni=i+move_aex
							count_n+=1

				else:
					i=ni
					move_aex=MOVE_AEX/2
				print('Adjust Pos:\t'+str(ni))
				axe(ni,dely,bias)
				time.sleep(3)
				old_green=green
				green=find_green(get_screen_arry(CROP1))
			print('Time:\t'+str(time.time()-START))
			print('Rounds:\t'+str(rounds+1))
			if rounds>=5:break
			if time.time()-START<=40 or (time.time()-START<=50 and rounds<=2):
				if IF_START==0:break
				time.sleep(2.35)
				mouse.move(910,625)
				mouse.left()
				time.sleep(0.25)
				START+=5
				rounds+=1
			else:
				if IF_START==0:break
				time.sleep(2.2)
				mouse.move(1010,625)
				mouse.left()
				time.sleep(1.6)
				break

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
			Thread(target=start_cutting).start()
		elif key._name_=='caps_lock':
			play_mp3(resource_path('end.mp3'))
			IF_START=0
			time.sleep(4)
			print('END CUTTING')
	except:
		pass

print('Press Caps to Start...')
IF_START=0
start_listen(on_press)