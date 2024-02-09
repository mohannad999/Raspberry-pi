from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
delay=0.1
BUTTON=20
REDLED=17
GPIO.setup(BUTTON,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(REDLED,GPIO.OUT)


LEDstate=0
buttonState=1
buttonStateOld=1

try :

	while True:
		buttonState=GPIO.input(BUTTON)
		print(buttonState)
		if buttonState==1 and buttonStateOld==0:
			LEDstate=not LEDstate
			GPIO.output(REDLED,LEDstate)
		buttonStateOld=buttonState

		sleep(delay)
except KeyboardInterrupt:
	GPIO.cleanup()
	print("GPIO Ready to Go")
