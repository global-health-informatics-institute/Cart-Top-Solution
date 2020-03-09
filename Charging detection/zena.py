import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.IN)

#GPIO.setup(23, GPIO.OUT)
#GPIO.setup(23, GPIO.HIGH)

time.sleep(2)

states = GPIO.input(24)

print (states)

time.sleep(2)