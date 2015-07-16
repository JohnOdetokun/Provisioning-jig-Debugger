import RPi.GPIO as GPIO
import logging

class Button:
    def __init__(self, logger=logging.getLogger(__name__)):
        self.logger = logger
        logging.basicConfig(level=logging.DEBUG)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    def __enter__(self):
        return self

    def wait_for_button_press(self):
        logging.debug("Waiting for button press")
        GPIO.wait_for_edge(11, GPIO.RISING)
        
        
    def __exit__(self, type, value, traceback):
        logging.debug("Button exit")
