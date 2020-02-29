# from playsound import playsound
from threading import Thread
from pygame import mixer
import time

def play_(name):
	mixer.init()
	mixer.music.load(name)
	mixer.music.play()
	time.sleep(2)


def play_mp3(name):
	Thread(target=play_,args=(name,)).start()

if __name__=='__main__':
	play_mp3('start.mp3')