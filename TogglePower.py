import RPi.GPIO as GPIO
import time
import logging

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
        self.toggleOff()
        time.sleep(1)
        self.toggleOn()
        time.sleep(3)

    def __exit__(self, type, value, traceback):
        #GPIO.cleanup()
        logging.info("Power toggled!")
