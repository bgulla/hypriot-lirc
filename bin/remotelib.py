#!/usr/bin/python

import requests
import photocell

class remotelib():

    KEY_POWER="KEY_POWER"
    BASE_URL="default"


    colors=dict()
    colors['']= ""
    colors[''] = ""
    colors[''] = ""



    def __init__(self, PORT, PHOTOCELL_PIN):
        self.PORT = PORT
        self.PHOTOCELL_PIN = PHOTOCELL_PIN
        self.BASE_URL="http://localhost:" + self.PORT + "/bar/api/v1.0/remote/"

    def togglePower(self):
        url = self.BASE_URL + self.KEY_POWER
        requests.get(url)

    def power_on(self):

        # get the initial readout
        initial_light_val = photocell.get(self.PHOTOCELL_PIN)
        # toggle the light
        self.togglePower()
        new_light_val = photocell.get(self.PHOTOCELL_PIN)

        if (new_light_val > initial_light_val):
            # whoops it looks like we turned it off, turn it back on
            print "Whoops, toggling"
            self.togglePower()

    def power_off(self):
        # get the initial readout
        initial_light_val = photocell.get(self.PHOTOCELL_PIN)
        # toggle the light
        self.togglePower()
        new_light_val = photocell.get(self.PHOTOCELL_PIN)

        if (new_light_val < initial_light_val):
            # whoops it looks like we turned it off, turn it back on
            print "Whoops, toggling"
            self.togglePower()

# https://github.com/bgulla/pyKeezer/blob/6e7ee61ba39bc28ad89f1936219e61b7313060b9/www/remote.php

colorList=[
	["BTN_0","BTN_1","BTN_2","BTN_3"],
	["BTN_4","BTN_5","BTN_6","BTN_7"],
	["BTN_8","BTN_9","KEY_NUMERIC_0","KEY_NUMERIC_1"],
	["KEY_NUMERIC_2","KEY_NUMERIC_3","KEY_NUMERIC_4","KEY_NUMERIC_5"],
	["KEY_NUMERIC_6","KEY_NUMERIC_7","KEY_NUMERIC_8","KEY_NUMERIC_9"],
]
