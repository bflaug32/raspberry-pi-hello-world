import RPi.GPIO as GPIO
from flask import Flask, redirect, url_for

app= Flask(__name__)

#Use GPIO number instead of Pin number
GPIO.setmode(GPIO.BCM)
#Make GPIO 25 output
GPIO.setup(25, GPIO.OUT)

@app.route("/")
def control():
	#control() returns a control
        # WARNING BE SURE YOU LINK TO YOUR OWN IP ADDRESS
        # e.g. replace the 172.16.37.207 with your own ip (from ifconfig) below
	return """
        <html>
        <head>
        </head>
        <body>

        <!--HOW TO SETUP A PICTURE/IMAGE LINK -->
        <a href="http://172.16.37.207:5000/on">
         <img src="https://s-media-cache-ak0.pinimg.com/736x/cb/06/cf/cb06cfc39ac3d3c2774433694f47660e.jpg" /img>
        </a>

        <!--HOW TO SETUP A TEXT LINK.. -->
        <a href="http://172.16.37.207:5000/off"> OFF </a>
        
        </body>
        </html>
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

