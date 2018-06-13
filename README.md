# IR Remote Control via REST 
![Screenshot](https://github.com/bgulla/hypriot-lirc/blob/master/img/screenshot.png?raw=true)
LIRC is hard, clunky and not very web friendly. This docker will stand up a webservice to send commands to LIRC via a simple curl command. 

# Prerequisites (to be completed on host, not docker)
```echo 'lirc_dev' >> /etc/modules ```

```echo 'lirc_rpi gpio_in_pin=18 gpio_out_pin=17' >> /etc/modules ```

```echo 'dtoverlay=lirc-rpi,gpio_in_pin=18,gpio_out_pin=17' >> /boot/config.txt```

be sure to change the pin number to reflect your hardware setup.




# Web UI 
Visit the web interface at http://pi:8080. 
# API
```bash
#http://pi:8080/api/<cmd_code>
curl http://pi:8080/KEY_POWER
```
# Building
```docker build -t blgulla/rpi-lirc .```

# Running
```bash
docker run --rm -t \
  -p 8080:8080 -p 9001:9001 \
  -v ${PWD}/conf/hardware.conf:/etc/lirc/hardware.conf \
  -v ${PWD}/conf/lircd.conf:/etc/lirc/lircd.conf \
  --privileged bgulla/rpi-lirc
```

