import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
myPwm = GPIO.PWM(17, 100)  # Set PWM frequency to 100 Hz

try:
    myPwm.start(90)  # Start PWM with 90% duty cycle
    while True:
        time.sleep(1)  # Sleep for 1 second
        myPwm.ChangeDutyCycle(3)  # Change duty cycle to 3%
        time.sleep(1)		 # Sleep for 1 second again
				 # If you want to stop and start PWM with different duty cycles,
	        		# you can do it here with myPwm.stop() followed by myPwm.start(new_duty_cycle)
except KeyboardInterrupt:
    myPwm.stop()  # Stop PWM
    GPIO.cleanup()  # Clean up GPIO
    print("GPIO cleaned up and ready to go")

