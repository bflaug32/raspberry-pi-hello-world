import RPi.GPIO as GPIO
from time import sleep

#Use GPIO number instead of Pin number
GPIO.setmode(GPIO.BCM)
#Make GPIO 25 output
GPIO.setup(25, GPIO.OUT)

try:
    while True:
            GPIO.output(25, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(25, GPIO.LOW)
            sleep(0.5)

#No error occurs when Ctrl+C is pushed.         
except KeyboardInterrupt:
    pass
    
#Release GPIO     
GPIO.cleanup()
