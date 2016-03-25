# IR Remote Control via REST 
LIRC is hard, clunky and not very web friendly. This docker will stand up a webservice to send commands to LIRC via a simple curl command. 

# Prerequisites
``` echo ```

# Building
```docker build -t blgulla/hypriot-lirc .```

# Running
```docker run -t --device "/dev/lirc0:/dev/lirc0" blgulla/hypriot-lirc ```
