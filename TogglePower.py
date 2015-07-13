import RPi.GPIO as GPIO
import time

class Reset:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(15,GPIO.OUT)
        GPIO.setwarnings(False)
        GPIO.output(15,1)

    def __enter__(self):
        return self

    def toggleOn(self):
        GPIO.output(15,1)

    def toggleOff(self):
        GPIO.output(15,0)

    def toggle(self):
        GPIO.output(15,1)
        time.sleep(1)
        GPIO.output(15,0)

    def __exit__(self, type, value, traceback):
        GPIO.cleanup()
