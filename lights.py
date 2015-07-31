import RPi.GPIO as GPIO
import time
import logging

class Lights:
    def __init__(self, logger=logging.getLogger(__name__)):
        self.logger = logger
        logging.basicConfig(level=logging.DEBUG)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        #success LED
        GPIO.setup(13,GPIO.OUT)
        GPIO.output(13,0)
        #Busy LED
        GPIO.setup(7,GPIO.OUT)
        GPIO.output(7,0)
        #fail LED
        GPIO.setup(12,GPIO.OUT)
        GPIO.output(12,0)
        #GPIO.setup(15,GPIO.OUT)
        #GPIO.output(15,1)
        logging.info("LEDS initialised")
        
    def __enter__(self):
        return self

    def busyOff(self):
        GPIO.output(7,0)

    def busy(self):
        GPIO.output(7,1)

    def success(self):
        for _ in range(6):
            GPIO.output(13,1)
            time.sleep(0.3)
            GPIO.output(13,0)
            time.sleep(0.3)
        logging.info("Flashed success LED")

    def failed(self):
        for _ in range(6):
            GPIO.output(12,1)
            time.sleep(0.3)
            GPIO.output(12,0)
            time.sleep(0.3)
        logging.info("Flashed failed LED")

    def clean(self):
        GPIO.cleanup()
        
    def __exit__(self, type, value, traceback):
        logging.info("lights exited")
        GPIO.cleanup()
