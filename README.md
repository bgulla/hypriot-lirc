# IR Remote Control via REST 
![Screenshot](https://github.com/bgulla/hypriot-lirc/blob/master/img/screenshot.png?raw=true)
LIRC is hard, clunky and not very web friendly. This docker will stand up a webservice to send commands to LIRC via a simple curl command. 

# Prerequisites
``` todo ```

# Web UI 
todo
# API
todo
# Building
```docker build -t blgulla/hypriot-lirc .```

# Running
```docker run -t --privileged  blgulla/hypriot-lirc ```


lirc_dev
lirc_rpi gpio_in_pin=23 gpio_out_pin=22
dtoverlay=lirc-rpi,gpio_out_pin=22

