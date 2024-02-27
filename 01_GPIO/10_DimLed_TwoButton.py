import RPi.GPIO as GPIO
from time import sleep
delay=0.1
button1=21
button2=20

button1_state=1
button1_state_old=1

button2_state=1
button2_state_old=1

Ledpin=17
DutyCycle=99
Freq=1000
GPIO.setmode(GPIO.BCM)
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(Ledpin,GPIO.OUT)

myPWM=GPIO.PWM(Ledpin,Freq)
myPWM.start(DutyCycle)
try:
	while True:
		button1_state=GPIO.input(button1)
		button2_state=GPIO.input(button2)

		if button1_state_old==0 and button1_state==1:
			#DutyCycle=DutyCycle-10
			DutyCycle=DutyCycle/2
			print('Dim Event')

		if button2_state_old==0 and button2_state==1:
			#DutyCycle=DutyCycle+10
			DutyCycle=DutyCycle*2
			print('Bright Event')

		if DutyCycle >99:
			DutyCycle=99
		if DutyCycle <0:
			DutyCycle=0

		#myPWM.ChangeDutyCycle(DutyCycle)
		myPWM.ChangeDutyCycle(int(DutyCycle))
		button1_state_old=button1_state
		button2_state_old=button2_state
		sleep(delay)
except KeyboardInterrupt:
	myPWM.stop()
	GPIO.cleanup()
	print('GPIO GOOD TO GO ')
