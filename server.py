import RPi.GPIO as GPIO
from time import sleep
from flask import Flask

app= Flask(__name__)

#Use GPIO number instead of Pin number
GPIO.setmode(GPIO.BCM)
#Make GPIO 25 output
GPIO.setup(25, GPIO.OUT)

@app.route("/")
def home():
	#home() returns a homepage
	return "Hello, visit yoursite.com/on to turn on a light."

@app.route("/on")
def on():
	#on() will turn on a light and display a message
	GPIO.output(25, GPIO.HIGH)
	return "The light is on. (visit yoursite.com/off to turn off)"

@app.route("/off")
def off():
	#off() will turn off a light and display a message
	GPIO.output(25, GPIO.LOW)
	return "The light is off."

if __name__ == "__main__":
	try:
		# Run the app.
		app.run(host='0.0.0.0')
	except KeyboardInerrupt:
		# if the user kills the app, shutdown the pinout mode
		GPIO.cleanup()

