from time import sleep
import RPi.GPIO as GPIO

delay=0.1
Button=21
RedLed=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(RedLed,GPIO.OUT) 
GPIO.setup(Button,GPIO.IN)

try:

	while True:
		readVal=GPIO.input(Button)
		if readVal==1:
			GPIO.output(RedLed,0)
		if readVal==0:
			GPIO.output(RedLed,1)
except KeyboardInterrupt:
	GPIO.cleanup()
	print('this all Folks')

