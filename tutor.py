import lib.key as key
import lib.mouse as mouse
import time


while 1:
	time.sleep(2)


	key.press('U')
	time.sleep(0.02)
	key.release('U')
	time.sleep(1)
	mouse.move(430,680)
	mouse.left()
	time.sleep(1)
	mouse.move(1480,695)
	mouse.left()
	time.sleep(13)


	key.press('Tab')
	time.sleep(0.02)
	key.release('Tab')
	time.sleep(0.02)
	key.press('W')
	time.sleep(4)
	key.release('W')

	key.press('1')
	time.sleep(0.02)
	key.release('1')

	time.sleep(2.36)

	key.press('2')
	time.sleep(0.02)
	key.release('2')

	time.sleep(2.36)

	key.press('Ctrl')
	key.press('2')
	time.sleep(0.02)
	key.release('2')
	key.release('Ctrl')

	time.sleep(3.5)
	key.press('U')
	time.sleep(0.02)
	key.release('U')
	time.sleep(0.5)
	mouse.move(200,170)
	mouse.left()
	time.sleep(0.5)
	mouse.move(900,550)
	mouse.left()
	time.sleep(5)