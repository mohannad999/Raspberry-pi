from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
delay=0.1
BUTTON=20
REDLED=17
GPIO.setup(BUTTON,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(REDLED,GPIO.OUT)

try :

	while True:
		readVal=GPIO.input(BUTTON)
		print(readVal)
		if readVal==1:
			GPIO.output(REDLED,0)
		if readVal==0:
			GPIO.output(REDLED,1)
		sleep(delay)
except KeyboardInterrupt:
	GPIO.cleanup()
	print("GPIO Ready to Go")
