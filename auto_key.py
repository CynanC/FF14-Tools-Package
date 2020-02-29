# -*- coding: utf-8 -*-  

from tkinter import *
from threading import Thread
from pynput import keyboard
import time
# from ctypes import *
import json
import os
from lib.listen_key import *
from lib.play_mp3 import play_mp3


skill_text='{\r\n\
	"黑骑": \r\n\
	[\r\n\
		{"skill_name": "伤害连-暗技-1", "skill_sequence": ["1", 2.4, "3", 1, "ctrl+`", 1.4, "ctrl+3", 2.4], "bind_key": "F1"}, \r\n\
		{"skill_name": "伤害连-暗技-2", "skill_sequence": ["1", 1, "ctrl+`", 1.5, "3", 1, "ctrl+`", 1.5, "ctrl+3", 2.5], "bind_key": "F2"}, \r\n\
		{"skill_name": "仇恨连-暗技", "skill_sequence": ["1", 2.5, "2", 1, "ctrl+`", 1.5, "ctrl+2"], "bind_key": "F3"}\r\n\
	], \r\n\
	"武士": \r\n\
	[\r\n\
		{"skill_name": "WS1", "skill_sequence": [], "bind_key": "F1"}, \r\n\
		{"skill_name": "WS2", "skill_sequence": [], "bind_key": "F2"}\r\n\
	]\r\n\
}'

try:
	fp=open('skill_list.txt','r')
	skill_text=fp.read()
	fp.close()
except:
	fp=open('skill_list.txt','w')
	fp.write(skill_text)
	fp.close()


skill_list=json.loads(skill_text)

root = Tk()
root.title("FF14 按键宏")
# root.iconbitmap(resource_path('favicon.ico'))
root.resizable(0,0)
bt=[]
bind_list={}


key=keyboard.Controller()
KEYCODE=['alt', 'alt_l', 'alt_r', 'backspace', 'caps_lock', 'cmd', 'cmd_r', 'ctrl', 'ctrl_l', 
'ctrl_r', 'delete', 'down', 'end', 'enter', 'esc', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 
'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 
'home', 'insert', 'left', 'menu', 'num_lock', 'page_down', 'page_up', 'pause', 'print_screen',
 'right', 'scroll_lock', 'shift', 'shift_r', 'space', 'tab', 'up']

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        relative_path='lib/'+relative_path
    return os.path.join(base_path, relative_path)


def press(key_code):
	if key_code in KEYCODE:
		key_code=keyboard.Key[key_code]
	key.press(key_code)

def  release(key_code):
	if key_code in KEYCODE:
		key_code=keyboard.Key[key_code]
	key.release(key_code)

def on_press(key):
	# print (key)
	if 'root' not in globals():
		return False
		# for i in skill_list:
	try:
		if key._name_=='caps_lock':button_act(0)
		v_n=1
		for i in skill_list:
			if v_n==v.get():
				for j in skill_list[i]:
					if key._name_==j['bind_key'].lower():
						button_act(j['num'],j['skill_sequence'])
				break
			v_n+=1
	except:
		pass


def button_act(num,*sk):
	if bt[num].state==0:
		play_mp3(resource_path('start.mp3'))
		if num!=0:
			for i in range(1,len(bt)):
				if i==num:continue
				if bt[i].state==1:button_act(i)
		bt[num].state=1
		bt[num]['relief']=SUNKEN
		if num==0:
			bt[num]['text']='总循环-开'
		else:
			try:
				Thread(target=skill_start,args=(num,sk[0],)).start()
			except:
				pass
				
	else:
		play_mp3(resource_path('end.mp3'))
		bt[num].state=0
		bt[num]['relief']=RAISED
		if num==0:
			bt[num]['text']='总循环-关'

def sleep_break(num,t):
	if bt[num]['relief']==RAISED:
		return 1
	time.sleep(t)
	if bt[num]['relief']==RAISED:
		return 1
	return 0

def skill_start(num,skill_sequence):
	print (skill_sequence)
	for i in skill_sequence:
		if not isinstance(i,str):
			if sleep_break(num,i):
				break
			continue
		sp_i=i.split("+")
		for j in sp_i:
			press(j)
		for j in sp_i:
			time.sleep(0.03)
			release(j)
	if bt[num].state==1 and bt[0].state==1:
		skill_start(num,skill_sequence)
	elif bt[num].state==1:
		button_act(num)


	
Label(root,text = "总循环:").grid(row = 0, column = 0,padx=10,pady=10)
bt.append(Button(root, text = "总循环-关",command = lambda:button_act(0)))
bt[0].grid(row = 0, column = 1,padx=10,pady=10)
bt[0].state=0

t_row=1
t_col=1
max_col=1
bt_num=1
v = IntVar()
v.set(1)
for s_name in skill_list:
	Label(root,text = s_name).grid(row = t_row, column = 0,padx=10,pady=10)
	for s_val in skill_list[s_name]:
		# print (s_val)
		bt.append(Button(root, text = s_val['skill_name'],command = lambda x=bt_num,y=s_val['skill_sequence'] :button_act(x,y)))
		bt[bt_num].grid(row=t_row,column=t_col,padx=10,pady=10)
		bt[bt_num].state=0
		skill_list[s_name][t_col-1]['num']=bt_num
		t_col+=1
		bt_num+=1
		if t_col>max_col:max_col=t_col
	t_row+=1
	t_col=1
t_row=1
for s_name in skill_list:
	Radiobutton(root,variable = v,value=t_row).grid(row=t_row,column=max_col,padx=10,pady=10)
	t_row+=1

thread_listen(on_press)

root.mainloop()
del root