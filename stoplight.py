import RPi.GPIO as GPIO
from time import sleep

#Setup the board's output
GPIO.setmode(GPIO.BCM)


#pin 25 is yellow, red is 18, green is 12
GPIO.setup(12, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)


try:
    while True:
            light_to_turn_on = raw_input("Which light do you want to turn on? (R,Y,G,B,C)")

            GPIO.output(12, GPIO.LOW)
            GPIO.output(25, GPIO.LOW)
            GPIO.output(18, GPIO.LOW)

            if light_to_turn_on.upper() == "B":
                GPIO.output(18, GPIO.HIGH)
                sleep(1)
                GPIO.output(18, GPIO.LOW)
                GPIO.output(25, GPIO.HIGH)
                sleep(1)
                GPIO.output(25, GPIO.LOW)
                GPIO.output(12, GPIO.HIGH)
            elif light_to_turn_on.upper() == "C":
                blink = int(raw_input("How Long to Blink?"))
                while blink > 0:
                    GPIO.output(25, GPIO.HIGH)
                    sleep(1)
                    GPIO.output(25, GPIO.LOW)
                    sleep(1)
                    blink -= 1  
            elif light_to_turn_on.upper() == "R":
                GPIO.output(18, GPIO.HIGH)
            elif light_to_turn_on.upper() == "G":
                GPIO.output(12, GPIO.HIGH)
            else:
                GPIO.output(25, GPIO.HIGH)
                                

#No error occurs when Ctrl+C is pushed.         
except KeyboardInterrupt:
    pass
    
#Release GPIO     
GPIO.cleanup()
