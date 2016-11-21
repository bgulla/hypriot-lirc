import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setmode(GPIO.BCM)


def get(PIN):
    return RCtime(PIN)


def RCtime(RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    # This takes about 1 millisecond per loop cycle
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading


if __name__ == "__main__":
    while True:
        print RCtime(18)
