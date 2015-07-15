import RPi.GPIO as GPIO
import logging
from lights import Lights

class Button:
    def __init__(self):
        logging.basicConfig()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        self.mode = 0;

    def __enter__(self):
        return self

    def butpush(self):
        try:
            GPIO.wait_for_edge(11, GPIO.RISING)
        except KeyboardInterrupt:
            with Lights as light:
                light.failed()
                logging.critical("Button error")
        
        
    def __exit__(self, type, value, traceback):
        #GPIO.cleanup()
        logging.info("Button class closed")
