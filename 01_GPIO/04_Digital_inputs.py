import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
inPin=21
GPIO.setup(inPin,GPIO.IN)
readVal=GPIO.input(inPin)
print(readVal)
GPIO.cleanup()

