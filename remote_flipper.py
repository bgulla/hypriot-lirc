#!/usr/bin/env python
import requests
import RPi.GPIO as GPIO
import time
import os 
import RPi.GPIO as GPIO, time, os      
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading


def read_photocell():
	return RCtime(25)


def toggleLEDPower():
	response = requests.get('http://localhost:8002/bar/api/v1.0/remote/KEY_POWER')


def turn_on_led():
	# get the initial readout
	initial_light_val = read_photocell()
	# toggle the light
	toggleLEDPower()
	new_light_val = read_photocell()
	
	if ( new_light_val > initial_light_val ):
		# whoops it looks like we turned it off, turn it back on
		print "Whoops, toggling"
		toggleLEDPower()

def turn_off_led():
	# get the initial readout
	initial_light_val = read_photocell()
	# toggle the light
	toggleLEDPower()
	new_light_val = read_photocell()
	
	if ( new_light_val < initial_light_val ):
		# whoops it looks like we turned it off, turn it back on
		print "Whoops, toggling"
		toggleLEDPower()


if ( len(sys.argv) >= 2 ):
	param = sys.argv[1]
	if param == "on":
		turn_on_led()
	if param == "off": 
		turn_off_led()
else:
	print "[Usage] remote_flipper.py [on|off]"
