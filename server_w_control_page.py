import RPi.GPIO as GPIO
from flask import Flask, redirect, url_for

app= Flask(__name__)

#Use GPIO number instead of Pin number
GPIO.setmode(GPIO.BCM)
#Make GPIO 25 output
GPIO.setup(25, GPIO.OUT)

@app.route("/")
def control():
	#control() returns a control page with buttons
	return """
        <!DOCTYPE html>
        <a href="/on"><img src="https://cdn.pixabay.com/photo/2016/06/01/07/41/green-1428507_960_720.png" height=300 width=300 /img></a>

        <a href="/off"><img src="https://cdn.pixabay.com/photo/2013/07/13/10/20/cigarette-lighter-156994_960_720.png" height=300 width=300 /img></a>
        """

@app.route("/on")
def on():
	#on() will turn on a light and redirect to the control page
	GPIO.output(25, GPIO.HIGH)
	return redirect(url_for('control'))

@app.route("/off")
def off():
	#off() will turn off a light and redirect to the control page
	GPIO.output(25, GPIO.LOW)
	return redirect(url_for('control'))

if __name__ == "__main__":
	try:
		# Run the app.
		app.run(host='0.0.0.0')
	except KeyboardInerrupt:
		# if the user kills the app, shutdown the pinout mode
		GPIO.cleanup()

