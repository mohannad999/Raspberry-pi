import RPi.GPIO as GPIO
import time
count='Y'
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
while count=='Y':
	numBlink=int(input('how many Blinks do you wish For: ' ))
	for i in range(0,numBlink):
		GPIO.output(11,1)
		time.sleep(1)
		GPIO.output(11,0)
		time.sleep(1)
	cont=input('Do you want to Continue : (Y for Yes)')	
GPIO.cleanup()

