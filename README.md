# raspberry-pi-hello-world

A guide for getting started with Raspberry pi. For an "intro to raspberry pi" class at NextFab (http://www.nextfab.com)

# Buying a raspberry pi

If you want wifi, buy a raspberry pi 3 model B https://www.raspberrypi.org/products/raspberry-pi-3-model-b/

If you don't care about wifi or performance too much, buy whatever is cheapest...
you can pickup a raspberry pi zero for $5 but note you'll need at least $10 worth of adapters to hook it up to USB peripherals and HDMI displays. So maybe buy RasPi 1 or 2.

# Buying an SD Card.

* Read this short guide https://www.raspberrypi.org/documentation/installation/sd-cards.md
* I recommend a 32GB microSD card for those raspberry pis that support it. Amazon has many of these.

# Formatting your SD card, first run.

* https://www.raspberrypi.org/downloads/
* there are a couple good guides here. http://elinux.org/RPi_Easy_SD_Card_Setup
* I highly recommend raspbian... if you do install raspbian make sure you run raspi-config.
* https://www.raspberrypi.org/documentation/configuration/raspi-config.md
* Note the default user on a raspberry pi is named `pi` with the password `raspberry`
* IF YOU ARE STRUGGLING, COME FOR HELP https://www.meetup.com/Philly-Makers/

# terminal basics, running and installing programs

* [tab] - autocomplete
* `man` -show me a manual
* `which` - where is this thing installed
* `ls` - list the contents of the current directory
* `pwd` - print the current working directory
* `cd` - change directories
* `mv` - move a file
* `cp` - copy a file
* `sudo` - run as root user
* `sudo !!`- run the last command as the root user
* `apt-get install [program-name]` install a linux program
* `python my_file.py` run a pyton program
* `pip install [library name]` install a python dependency

* for more... check here > http://lifehacker.com/5633909/who-needs-a-mouse-learn-to-use-the-command-line-for-almost-anything
* or here > https://github.com/predbrad/brads-guides/tree/master/bash/docs

# using the raspberry pi as a calendar display

open [calendar.html](../calendar.html) in a web browser.

# blinking the LEDs

* hook up your LED to the correct pin (and ground)
* run blink.py  `cd [directory of file] && python blink.py`

# making a web server (roll your own)

* read through http://flask.pocoo.org/
* figure out your IP address with the command `ifconfig`
* start a basic server that shows `hello world`
* make an endpoint to turn on and off the LED, copy and paste the code from blink.py

# Making an arcade (for at home)

* install Retropie https://retropie.org.uk/
* read the wiki https://github.com/retropie/RetroPie-Setup/wiki
